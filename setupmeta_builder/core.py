# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
# all attrs from spec:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# ----------



from typing import *
from .abc import *
from collections import defaultdict
import logging
import itertools

from anyioc import ServiceProvider
from anyioc.g import get_namespace_provider
from toposort import toposort_flatten
from fsoopify import FileInfo, DirectoryInfo

from .utils import ensure_list

class _Project(IProject):
    def __init__(self, root_dir: str) -> None:
        super().__init__()
        self._root_dir = DirectoryInfo(root_dir)
        assert self._root_dir.is_directory(), f'{root_dir} is not a dir.'
        self._text_cached = {}

    @property
    def root_dir(self):
        'the root dir (abs)path of the project.'
        return self._root_dir

    def read_text(self, path: str, relative: bool=True, cached: bool=True) -> Optional[str]:
        f = self._root_dir.get_fileinfo(path) if relative else FileInfo(path)
        d = None
        if f.is_file():
            try:
                d = f.read_text()
            except FileNotFoundError:
                pass
        if cached:
            self._text_cached[f.path] = d
        return d


class _Context(IMetadataResolveContext):
    def __init__(self, project: IProject, logger: Logger) -> None:
        super().__init__()
        self._project = project
        self._logger = logger
        self._results: Dict[str, Metadata] = {}

    @property
    def project(self) -> IProject:
        return self._project

    @property
    def logger(self) -> Logger:
        return self._logger

    def set_result(self, name: str, result: Metadata):
        'set result with metadata name.'
        self._results[name] = result

    def get_results(self):
        return self._results


class SetupMeta:
    def __init__(self, ioc: ServiceProvider) -> None:
        super().__init__()
        self._metadatas_table: Dict[str, List[Metadata]] = {}
        self._ioc = ioc

    @property
    def metadatas_table(self):
        return self._metadatas_table

    def to_setup_attrs(self) -> dict:
        attrs = {}
        for name, metadatas in self._metadatas_table.items():
            picker: IAttrPicker = self._ioc.get(f'AttrPicker[{name}]') or self._ioc.get('AttrPicker')
            picker.write(name, metadatas, attrs)
        return attrs

def _sort_providers(providers: List[IMetadataProvider]) -> List[IMetadataProvider]:
    prov_map: DefaultDict[str, Set[int]] = defaultdict(set)
    for i, provider in enumerate(providers):
        for prov in ensure_list(provider.get_provided()):
            prov_map[prov].add(i)
    toposort_data: Dict[int, Set[int]] = {}

    dep_all = set()
    for i, provider in enumerate(providers):
        if '*' in provider.get_dependencies():
            dep_all.add(i)
    not_all = set(range(len(providers))) - dep_all

    for i, provider in enumerate(providers):
        if i in dep_all:
            toposort_data[i] = not_all.copy()
        else:
            toposort_data[i] = set(itertools.chain(*[prov_map[d] for d in ensure_list(provider.get_dependencies())]))

    sorted_indexes = toposort_flatten(toposort_data)
    return [providers[i] for i in sorted_indexes]

def build_setupmeta(root_dir: str):
    ioc = get_namespace_provider('setupmeta_builder').scope()
    sm = SetupMeta(ioc)
    providers: List[IMetadataProvider] = ioc.get_many('MetadataProvider')
    project = _Project(root_dir)

    # sort providers:
    sorted_providers = _sort_providers(providers)

    # call providers:
    metadatas_table: Dict[str, List[Metadata]] = defaultdict(list)

    def get_sorter(name: str) -> ISorter:
        return ioc.get(f'Sorter[{name}]') or ioc['Sorter']

    for provider in sorted_providers:
        provider_name = type(provider).__qualname__
        ctx = _Context(project, logger=logging.getLogger(provider_name))
        deps: Dict[str, List[Metadata]] = {}
        for name in ensure_list(provider.get_dependencies()):
            deps[name] = get_sorter(name).sort(name, metadatas_table[name]).copy()
        try:
            provider.run(ctx, deps)
        except Exception as e:
            ctx.logger.error(f'error raised when calling {provider_name}: {e}', exc_info=e)
        else:
            for name, metadata in ctx.get_results().items():
                metadata.metadata_id = f'{provider_name}:{name}'
                metadatas_table[name].append(metadata)

    # combine results:
    for name in metadatas_table:
        sm.metadatas_table[name] = get_sorter(name).sort(name, metadatas_table[name])

    return sm

if __name__ == '__main__':
    from pprint import pprint
    pprint(build_setupmeta('.').to_setup_attrs())


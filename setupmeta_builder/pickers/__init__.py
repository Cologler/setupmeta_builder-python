# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import itertools

from packaging.requirements import Requirement

from ..consts import *
from ..abc import *
from ..bases import *
from ..utils import ensure_list

def select_requirement(requirements: List[Requirement]) -> Requirement:
    assert requirements
    reqs = requirements.copy()
    if len(reqs) > 1 and any(not r.specifier for r in reqs):
        reqs = [r for r in reqs if not r.specifier]
    return reqs[0]

def sort_requirements(requirements: List[Requirement]) -> List[Requirement]:
    return sorted(requirements, key=lambda i: i.name)

def requirements_tostr(collected_requirements: List[Dict[str, Requirement]]) -> List[str]:
    grouped_requirements: Dict[str, List[Requirement]] = {}
    for requirements in collected_requirements:
        for name, requirement in requirements.items():
            grouped_requirements.setdefault(name, []).append(requirement)

    reqs = [select_requirement(rs) for rs in grouped_requirements.values()]
    return [str(r) for r in sort_requirements(reqs)]

class DefaultAttrPicker(IAttrPicker):
    def write(self, name: str, metadatas: List[Metadata], attrs: Dict[str, Any]):
        if not metadatas:
            return

        if name == MetaNames.long_description:
            metadata = metadatas[0]
            value: LongDescription = metadata.value
            attrs[MetaNames.long_description] = value.long_description
            if value.long_description_content_type:
                attrs[MetaNames.long_description_content_type] = value.long_description_content_type

        elif name == MetaNames.entry_points:
            for metadata in metadatas:
                if metadata.value:
                    entry_points: dict = attrs.setdefault(MetaNames.entry_points, {})
                    for k, v in metadata.value.items():
                        entry_points.setdefault(k, v)

        elif name == MetaNames.classifiers:
            classifiers = []
            for metadata in metadatas:
                assert isinstance(metadata.value, (list, str)), metadata.value
                classifiers.extend(ensure_list(metadata.value))
            attrs[name] = list(sorted(set(classifiers)))

        elif name in {MetaNames.install_requires, MetaNames.tests_require}:
            attrs[name] = requirements_tostr([m.value for m in metadatas])

        elif name == MetaNames.extras_require:
            extras_names: List[str] = list(set(itertools.chain(*[m.value for m in metadatas])))

            extras = {}
            for extra_name in extras_names:
                extras[extra_name] = requirements_tostr([m.value.get(extra_name, {}) for m in metadatas])

            if extras:
                attrs[name] = extras

        else:
            metadata = metadatas[0]
            attrs[name] = metadata.value

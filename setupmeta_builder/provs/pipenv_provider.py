# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from packaging.requirements import Requirement

from ..consts import *
from ..abc import *

def package_to_require(k, v):
    if v == '*':
        return Requirement(k)
    return Requirement(k+v)

@exported
class PipenvProvider(IMetadataProvider):
    def get_provided(self) -> Union[List[str], str]:
        return [
            MetaNames.install_requires,
            MetaNames.tests_require,
        ]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        pipfile_fi = context.project.root_dir.get_fileinfo('Pipfile')
        if not pipfile_fi.is_file():
            return

        def infer_from(field_path: str):
            return f'file <Pipfile> :: <{field_path}>'

        import pipfile
        pf = pipfile.load(str(pipfile_fi.path))

        def parse_dependencies(metaname: str, pf_key: str):
            requires = {}
            for k, v in pf.data[pf_key].items():
                requires[k] = package_to_require(k, v)
            if requires:
                context.set_result(metaname, Metadata(
                    priority=Priorities.IMPLICIT_SETTINGS,
                    value=requires,
                    infer_from=infer_from(pf_key)
                ))

        parse_dependencies(MetaNames.install_requires, 'default')
        parse_dependencies(MetaNames.tests_require, 'develop')

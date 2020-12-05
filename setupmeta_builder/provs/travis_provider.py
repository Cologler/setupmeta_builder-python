# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..consts import *
from ..consts_classifiers import PYTHON_CLASSIFIERS_TABLE
from ..abc import *

@exported
class TravisClassifiersProvider(IMetadataProvider):
    def get_provided(self) -> Union[List[str], str]:
        return MetaNames.classifiers

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        classifiers: List[str] = []
        travis_yaml = context.project.root_dir.get_fileinfo('.travis.yml')

        if travis_yaml.is_file():
            travis_conf = travis_yaml.load()
            pylist = travis_conf.get('python', [])
            python_classifiers_table = {z.short_name: z for z in PYTHON_CLASSIFIERS_TABLE}
            for py in pylist:
                if py in python_classifiers_table:
                    classifiers.append(python_classifiers_table[py].classifier)

        if classifiers:
            context.set_result(MetaNames.classifiers, Metadata(
                priority=Priorities.INFER,
                value=classifiers,
                infer_from='file <.travis.yml>'
            ))

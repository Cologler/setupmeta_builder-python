# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..consts import *
from ..abc import *

def get_default_values() -> Dict[str, Any]:
    values = {}
    values[MetaNames.zip_safe] = False
    values[MetaNames.include_package_data] = True
    return values

@exported
class DefaultProvider(IMetadataProvider):
    'the metadata provider base on git system.'
    def get_provided(self) -> List[str]:
        return list(get_default_values())

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        def set_result(name: str, value: Any):
            context.set_result(name, result=Metadata(
                priority=Priorities.DEFAULT,
                value=value,
                infer_from='default'
            ))

        for row in get_default_values().items():
            set_result(*row)

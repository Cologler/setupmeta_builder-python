# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..abc import *


class DefaultSorter(ISorter):
    def sort(self, name: str, metadatas: List[Metadata]) -> List[Metadata]:
        return sorted(metadatas, key=lambda m: -m.priority)

# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import os

from .consts import *
from .abc import *

def get_package_locations(deps: Dict[str, List[Metadata]]) -> Dict[str, str]:
    data_packages = deps[MetaNames.packages]
    data_package_dir = deps[MetaNames.package_dir]
    if not data_packages:
        return {}
    packages: List[str] = data_packages[0].value
    if data_package_dir:
        package_dir: Dict[str, str] = data_package_dir[0].value
    else:
        package_dir = {}
    rv = {}
    for package in packages:
        parts = package.split('.')
        package_relpath = os.path.join(*parts)
        src_dir = package_dir.get(parts[0])
        rv[package] = os.path.join(src_dir, package_relpath) if src_dir else package_relpath
    return rv

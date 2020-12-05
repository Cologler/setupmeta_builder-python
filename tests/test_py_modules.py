# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
from setupmeta_builder import get_setup_attrs

def test_py_modules():
    setup_attrs = get_setup_attrs(os.path.join('tests', 'only_mods_projs', 'mod1'))
    assert setup_attrs == {
        'py_modules': ['mod1'],
        'include_package_data': True,
        'zip_safe': False,
        'name': 'mod1'
    }

def test_py_modules_with_python_prefix():
    setup_attrs = get_setup_attrs(os.path.join('tests', 'only_mods_projs', 'python-mod2'))
    assert setup_attrs == {
        'py_modules': ['mod2'],
        'include_package_data': True,
        'name': 'mod2',
        'zip_safe': False,
    }

def test_py_modules_with_python_suffix():
    setup_attrs = get_setup_attrs(os.path.join('tests', 'only_mods_projs', 'mod3-python'))
    assert setup_attrs == {
        'py_modules': ['mod3'],
        'include_package_data': True,
        'name': 'mod3',
        'zip_safe': False,
    }

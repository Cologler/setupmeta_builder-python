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
        'classifiers': [],
        'entry_points': {},
        'include_package_data': True,
        'long_description': '',
        'name': 'mod1',
        'packages': [],
        'zip_safe': False,
    }

def test_py_modules_with_python_prefix():
    setup_attrs = get_setup_attrs(os.path.join('tests', 'only_mods_projs', 'python-mod2'))
    assert setup_attrs == {
        'py_modules': ['mod2'],
        'classifiers': [],
        'entry_points': {},
        'include_package_data': True,
        'long_description': '',
        'name': 'mod2',
        'packages': [],
        'zip_safe': False,
    }

def test_py_modules_with_python_suffix():
    setup_attrs = get_setup_attrs(os.path.join('tests', 'only_mods_projs', 'mod3-python'))
    assert setup_attrs == {
        'py_modules': ['mod3'],
        'classifiers': [],
        'entry_points': {},
        'include_package_data': True,
        'long_description': '',
        'name': 'mod3',
        'packages': [],
        'zip_safe': False,
    }

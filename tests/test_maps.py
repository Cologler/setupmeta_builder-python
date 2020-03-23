# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_py_classifiers_map():
    from setupmeta_builder.classifiers import PY_CLASSIFIERS_MAP
    assert PY_CLASSIFIERS_MAP['2.7'] == 'Programming Language :: Python :: 2.7'
    assert PY_CLASSIFIERS_MAP['3.3'] == 'Programming Language :: Python :: 3.3'

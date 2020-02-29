# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_get_global_funcnames():
    from fsoopify import FileInfo
    from setupmeta_builder.utils import get_global_funcnames

    funcnames = get_global_funcnames(FileInfo(__file__))
    assert 'test_get_global_funcnames' in funcnames
    for name in funcnames:
        assert name.startswith('test_')

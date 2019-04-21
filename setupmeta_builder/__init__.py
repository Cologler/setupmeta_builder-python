# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys

from .core import SetupAttrContext, SetupMetaBuilder

def get_setup_attrs(root_path=None) -> dict:
    '''
    get the auto generated attrs dict.
    '''
    ctx = SetupAttrContext(root_path)
    SetupMetaBuilder().fill_ctx(ctx)
    return ctx.setup_attrs

def setup_it(**attrs):
    '''
    just enjoy the auto setup!
    '''
    setup_attrs = get_setup_attrs()
    setup_attrs.update(attrs)

    if len(sys.argv) == 2 and sys.argv[1].lower() == 'print-attrs':
        from prettyprinter import pprint
        if 'long_description' in setup_attrs and len(setup_attrs['long_description']) > 1000:
            setup_attrs['long_description'] = '...<Hided for too long>...'
        pprint(setup_attrs)
        return

    from setuptools import setup
    setup(**setup_attrs)

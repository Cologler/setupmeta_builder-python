# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from setupmeta_builder.core import (
    SetupMetaBuilder
)

def test_setup_meta_builder_update_attrs_order():
    sorted_attrs = SetupMetaBuilder.will_update_attrs
    assert len(set(sorted_attrs)) == len(sorted_attrs), 'attrs should unique'

    def assert_order(before, after):
        sorted_attrs.index(before) > sorted_attrs.index(after)

    # name was parse from packages
    assert_order('packages', 'name')

    # classifiers was base from:
    # - license (License :: OSI Approved :: ?)
    # - version (Development Status :: ?)
    assert_order('license', 'classifiers')
    assert_order('version', 'classifiers')

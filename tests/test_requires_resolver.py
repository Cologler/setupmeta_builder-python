# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import fsoopify

from setupmeta_builder.core import SetupAttrContext
from setupmeta_builder.requires_resolver import (
    RequirementsTxtRequiresResolver,
    PipfileRequiresResolver,
    DefaultRequiresResolver,
)

install_requires = ['fsoopify', 'pipfile', 'pyyaml']
test_require = ['pytest']

def _get_non_module_ctx():
    ctx = SetupAttrContext('tests')
    return ctx

def test_requirements_txt_resolve_on_non_module():
    ctx = _get_non_module_ctx()
    resolver = RequirementsTxtRequiresResolver()
    assert resolver.resolve_install_requires(ctx) is None
    assert resolver.resolve_tests_require(ctx) is None

def test_requirements_txt_resolve_on_current_module():
    ctx = SetupAttrContext()
    resolver = RequirementsTxtRequiresResolver()
    assert resolver.resolve_install_requires(ctx) == install_requires
    assert resolver.resolve_tests_require(ctx) is None

def test_pipfile_resolve_on_non_module():
    ctx = _get_non_module_ctx()
    resolver = PipfileRequiresResolver()
    assert resolver.resolve_install_requires(ctx) is None
    assert resolver.resolve_tests_require(ctx) is None

def test_pipfile_resolve_on_current_module():
    ctx = SetupAttrContext()
    resolver = PipfileRequiresResolver()
    assert resolver.resolve_install_requires(ctx) == install_requires
    assert resolver.resolve_tests_require(ctx) == test_require

def test_default_resolve_on_current_module():
    ctx = SetupAttrContext()
    resolver = DefaultRequiresResolver()
    assert resolver.resolve_install_requires(ctx) == install_requires
    assert resolver.resolve_tests_require(ctx) == test_require

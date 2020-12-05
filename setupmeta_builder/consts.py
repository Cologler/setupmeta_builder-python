# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .utils import make_consts

EXCLUDED_PACKAGES = (
    # pytest:
    'tests', 'tests.*',
)


class Priorities:
    DEFAULT = 0

    # determine by {source|python} convention
    #
    # e.g. source convention
    # - README[.{md|rst}]
    # - .travis.yml
    # - src\*; lib\*
    #
    # e.g. python convention
    # - setuptools.find_packages()
    #
    # e.g. scm convention
    # - git tag (as version)
    INFER = 20

    # determine by setupmeta_builder convention (which is manual added by user)
    # e.g.
    # - entry_points_console_scripts.py
    INFER_SMB = 60

    # determine by configurations (which is manual added by user)
    # e.g.
    # - requirements.txt
    # - Pipfile (requirements)
    # - pyproject.toml (package info, requirements)
    IMPLICIT_SETTINGS = 80

    # determine by user explicit call
    # e.g.
    # - setupmeta_builder.setup(...)
    EXPLICIT_SETTINGS = 100


@make_consts
class MetaNames:
    packages: str
    package_dir: str
    py_modules: str
    long_description: str
    long_description_content_type: str
    name: str
    version: str
    author: str
    author_email: str
    url: str
    license: str
    classifiers: str
    scripts: str
    entry_points: str
    zip_safe: str
    include_package_data: str
    setup_requires: str
    install_requires: str
    tests_require: str
    extras_require: str

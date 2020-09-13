# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import tempfile

import fsoopify

from setupmeta_builder import get_setup_attrs

def test_poetry_extras():
    with tempfile.TemporaryDirectory() as tmpdir:
        root = fsoopify.DirectoryInfo(tmpdir)
        root.get_fileinfo('pyproject.toml').write_text(
'''
[tool.poetry]
name = "awesome"

[tool.poetry.dependencies]
# These packages are mandatory and form the core of this package’s distribution.
mandatory = "^1.0"

# A list of all of the optional dependencies, some of which are included in the
# below `extras`. They can be opted into by apps.
psycopg2 = { version = "^2.7", optional = true }
mysqlclient = { version = "^1.3", optional = true }

[tool.poetry.extras]
mysql = ["mysqlclient"]
pgsql = ["psycopg2"]
'''
        )
        setup_attrs = get_setup_attrs(tmpdir)
        assert setup_attrs == {
            'classifiers': [],
            'entry_points': {},
            'extras_require': {
                'mysql': ['mysqlclient<2.0,>=1.3'],
                'pgsql': ['psycopg2<3.0,>=2.7']
            },
            'include_package_data': True,
            'install_requires': [
                'mandatory<2.0,>=1.0'
            ],
            'long_description': '',
            'name': 'awesome',
            'packages': [],
            'zip_safe': False,
        }



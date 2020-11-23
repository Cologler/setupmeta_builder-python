# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import re

import fsoopify

from setupmeta_builder import get_setup_attrs

install_requires = fsoopify.FileInfo('requirements.txt').read_text().strip().splitlines()
install_requires.sort()

def test_attrs_for_setupmeta_builder():
    setup_attrs = get_setup_attrs()
    with open('README.md', encoding='utf-8') as fp:
        assert setup_attrs['long_description'] == fp.read()
    setup_attrs.pop('long_description')
    assert re.match(r'^\d+\.\d+\.\d+$', setup_attrs.pop('version'))

    classifiers = setup_attrs.pop('classifiers')
    assert isinstance(classifiers, list)
    assert 'Development Status :: 5 - Production/Stable' in classifiers
    assert 'License :: OSI Approved :: MIT License' in classifiers
    assert 'Programming Language :: Python :: 3.7' in classifiers
    assert 'Programming Language :: Python :: 3.8' in classifiers

    assert setup_attrs == {
        'packages': [
            'setupmeta_builder',
            'setupmeta_builder.cli',
            'setupmeta_builder.metadata_providers'
        ],
        'long_description_content_type': 'text/markdown',
        'name': 'setupmeta_builder',
        'author': 'Cologler',
        'author_email': 'skyoflw@gmail.com',
        'url': 'https://github.com/Cologler/setupmeta_builder-python',
        'license': 'MIT License',
        'zip_safe': False,
        'include_package_data': True,
        'install_requires': install_requires,
        'tests_require': ['pytest'],
        'entry_points': {}
    }

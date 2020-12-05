# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import fsoopify
import re
import functools

from packaging.version import Version, parse

def parse_homepage_from_git_url(git_url: str):
    'parse homepage url from a git url (or None if unable to parse)'

    # parse git@github.com:Cologler/setupmeta_builder-python.git
    # to https://github.com/Cologler/setupmeta_builder-python

    # parse https://github.com/Cologler/setupmeta_builder-python.git
    # to https://github.com/Cologler/setupmeta_builder-python

    match = re.match(r'^(?:(?:git\+)?(?:ssh|https)://)?(?:git@)?(?P<host>github.com)[\:/](?P<user>[^/]+)/(?P<repo>[^/\.]+)(?:\.git)?$', git_url)
    if match:
        host = match.group('host')
        user = match.group('user')
        repo = match.group('repo')
        return f'https://{host}/{user}/{repo}'
    return None

def get_field(d: dict, path: str, default=None):
    '''
    example: get_field(pyproject, 'tool.poetry.version')
    '''

    parts = path.split('.')
    for field in parts[:-1]:
        d = d.get(field, {})
    return d.get(parts[-1], default)

def make_consts(cls: type):
    type_hints = get_type_hints(cls)
    for name, type_ in type_hints.items():
        if not hasattr(cls, name) and type_ is str:
            setattr(cls, name, name)
    return cls

def parse_version(version: str) -> Version:
    v = parse(version)
    if isinstance(v, Version):
        return v

def ensure_list(value: Union[List[str], str]) -> List[str]:
    return [value] if isinstance(value, str) else list(value)

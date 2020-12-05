# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_parse_homepage_from_git_url():
    from setupmeta_builder.utils import parse_homepage_from_git_url

    assert parse_homepage_from_git_url('https://github.com/Cologler/setupmeta_builder-python.git') ==\
        'https://github.com/Cologler/setupmeta_builder-python'

    assert parse_homepage_from_git_url('git@github.com:Cologler/setupmeta_builder-python.git') ==\
        'https://github.com/Cologler/setupmeta_builder-python'

    assert parse_homepage_from_git_url('git+https://github.com/npm/hosted-git-info.git') ==\
        'https://github.com/npm/hosted-git-info'

    assert parse_homepage_from_git_url('git+ssh://git@github.com/npm/hosted-git-info.git') ==\
        'https://github.com/npm/hosted-git-info'

    assert parse_homepage_from_git_url('git@github.com:npm/hosted-git-info.git') ==\
        'https://github.com/npm/hosted-git-info'

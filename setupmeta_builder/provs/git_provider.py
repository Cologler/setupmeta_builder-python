# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import subprocess
import os

from ..consts import *
from ..abc import *
from ..utils import parse_homepage_from_git_url, parse_version

def get_git_output(root_dir: str, argv: list) -> Optional[str]:
    git_dir = os.path.join(root_dir, '.git')
    argv = ['git', f'--git-dir={git_dir}'] + argv
    proc = subprocess.run(argv,
        encoding='utf-8',
        cwd=root_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if proc.returncode == 0:
        return proc.stdout.strip()

def get_origin_url(root_dir: str):
    origin_url = None
    git_remote_stdout = get_git_output(root_dir, ['remote'])
    if git_remote_stdout:
        lines = git_remote_stdout.splitlines()
        if 'origin' in lines:
            origin_url = get_git_output(root_dir, ['remote', 'get-url', 'origin'])
    return origin_url

def get_tag(root_dir: str):
    git_describe_stdout = get_git_output(root_dir, ['describe', '--tags'])
    if git_describe_stdout:
        return git_describe_stdout.split('-')[0]

@exported
class GitProvider(IMetadataProvider):
    'the metadata provider base on git system.'
    def get_provided(self) -> List[str]:
        return [MetaNames.url, MetaNames.version]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        root_dir = str(context.project.root_dir.path)

        origin_url = get_origin_url(root_dir)
        if origin_url:
            homepage_url = parse_homepage_from_git_url(origin_url)
            if homepage_url:
                context.set_result(MetaNames.url, Metadata(
                    priority=Priorities.INFER,
                    value=homepage_url,
                    infer_from='git remote get-url origin'
                ))

        tag = get_tag(root_dir)
        if tag:
            version = parse_version(tag)
            if version:
                context.set_result(MetaNames.version, Metadata(
                    priority=Priorities.INFER,
                    value=str(version),
                    infer_from='git describe --tags'
                ))

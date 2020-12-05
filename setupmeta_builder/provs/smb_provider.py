# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import os
import json
import re

from packaging.requirements import Requirement
from fsoopify import Path

from ..consts import *
from ..abc import *

@exported
class SMBProvider(IMetadataProvider):
    def get_provided(self) -> Union[List[str], str]:
        return [
            MetaNames.author,
            MetaNames.author_email,
            MetaNames.extras_require,
        ]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        global_conf_text = context.project.read_text(Path.from_home() / '.pkgit.json', relative=False)
        global_conf = json.loads(global_conf_text) if global_conf_text else {}

        cwd_conf_text = context.project.read_text('.pkgit.json')
        cwd_conf = json.loads(cwd_conf_text) if cwd_conf_text else {}

        pkgit_conf = ChainMap(cwd_conf, global_conf)

        author_name = pkgit_conf.get('author')
        if author_name:
            context.set_result(MetaNames.author, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=author_name,
                infer_from=f'file <.pkgit.json>'
            ))

        author_email = pkgit_conf.get('author_email')
        if author_email:
            context.set_result(MetaNames.author_email, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=author_email,
                infer_from=f'file <.pkgit.json>'
            ))

        root_path = str(context.project.root_dir.path)
        extras_require = {}
        for fn in os.listdir(root_path):
            match = re.match(r'^requirements\.(?P<name>.+)\.txt$', fn, re.I)
            if match:
                extra_name = match['name']
                requirements_text = context.project.read_text(fn)
                requirements = [Requirement(l) for l in requirements_text.splitlines() if l]
                extras_require[extra_name] = {r.name: r for r in requirements}
        if extras_require:
            context.set_result(MetaNames.extras_require, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=extras_require,
                infer_from=f'file <requirements.*.txt>'
            ))

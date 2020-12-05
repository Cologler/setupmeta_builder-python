# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import re

from packaging.requirements import Requirement
try:
    from poetry.core.semver import parse_constraint
except ModuleNotFoundError:
    from poetry.semver import parse_constraint

from ..consts import *
from ..consts_classifiers import LICENSE_CLASSIFIERS_TABLE
from ..abc import *
from ..utils import get_field

RE_AUTHORS = re.compile('^(?P<name>.+) <(?P<email>.+@.+)>$')

def parse_author(author: str) -> Tuple[str, str]:
    author = author.strip()
    match = RE_AUTHORS.match(author)
    if match:
        author_name, author_email = match.group('name'), match.group('email')
        return author_name, author_email
    return author, None

def get_requirements(items: dict, inculde_optional) -> Dict[str, Requirement]:
    rv = {}
    for k, v in items.items():
        vc = None

        if isinstance(v, str):
            vc = parse_constraint(v)

        elif isinstance(v, dict):
            if not v.get('optional') or inculde_optional:
                version = v.get('version')
                if isinstance(version, str):
                    vc = parse_constraint(version)

        else:
            raise NotImplementedError(type(v))

        if vc:
            vcs = str(vc)
            if vcs == '*':
                rv[k] = Requirement(k)
            else:
                rv[k] = Requirement(k + vcs)

    return rv

@exported
class PoetryProvider(IMetadataProvider):

    def get_provided(self) -> Union[List[str], str]:
        return [
            MetaNames.version,
            MetaNames.author,
            MetaNames.author_email,
            MetaNames.url,
            MetaNames.entry_points,
            MetaNames.classifiers,
            MetaNames.license,
            MetaNames.name,
            MetaNames.install_requires,
            MetaNames.tests_require,
            MetaNames.extras_require,
        ]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        pyproject = context.project.root_dir.get_fileinfo('pyproject.toml')
        if not pyproject.is_file():
            return
        pyproject_data = pyproject.load()

        def infer_from(field_path: str):
            return f'file <pyproject.toml> :: <{field_path}>'

        package_name = get_field(pyproject_data, 'tool.poetry.name')
        if isinstance(package_name, str) and package_name:
            context.set_result(MetaNames.name, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=package_name,
                infer_from=infer_from('tool.poetry.authors')
            ))

        authors = get_field(pyproject_data, 'tool.poetry.authors', [])
        if authors:
            author_name, author_email = parse_author(authors[0])
            if author_name:
                context.set_result(MetaNames.author, Metadata(
                    priority=Priorities.IMPLICIT_SETTINGS,
                    value=author_name,
                    infer_from=infer_from('tool.poetry.authors')
                ))
            if author_email:
                context.set_result(MetaNames.author_email, Metadata(
                    priority=Priorities.IMPLICIT_SETTINGS,
                    value=author_email,
                    infer_from=infer_from('tool.poetry.authors')
                ))

        version = get_field(pyproject_data, 'tool.poetry.version')
        if version:
            context.set_result(MetaNames.version, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=version,
                infer_from=infer_from('tool.poetry.version')
            ))

        homepage = get_field(pyproject_data, 'tool.poetry.homepage')
        if homepage:
            context.set_result(MetaNames.url, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value=version,
                infer_from=infer_from('tool.poetry.homepage')
            ))

        scripts = get_field(pyproject_data, 'tool.poetry.scripts')
        if isinstance(scripts, dict) and scripts:
            context.set_result(MetaNames.entry_points, Metadata(
                priority=Priorities.IMPLICIT_SETTINGS,
                value={
                    'console_scripts': [f'{k}={v}' for k, v in scripts.items()]
                },
                infer_from=infer_from('tool.poetry.homepage')
            ))

        license_id = get_field(pyproject_data, 'tool.poetry.license')
        if license_id:
            for li in LICENSE_CLASSIFIERS_TABLE:
                if li.spdx_id == license_id:
                    context.set_result(MetaNames.classifiers, Metadata(
                        priority=Priorities.IMPLICIT_SETTINGS,
                        value=li.classifier,
                        infer_from=infer_from('tool.poetry.license')
                    ))
                    break
            else:
                context.set_result(MetaNames.license, Metadata(
                    priority=Priorities.IMPLICIT_SETTINGS,
                    value=license_id,
                    infer_from=infer_from('tool.poetry.license')
                ))

        def parse_dependencies(metaname: str, scope: str):
            field = f'tool.poetry.{scope}'
            dependencies = get_field(pyproject_data, field)
            if dependencies:
                requirements = get_requirements(dependencies, False)
                python_ver = requirements.pop('python', None) # currently ignore
                context.set_result(metaname, Metadata(
                    priority=Priorities.IMPLICIT_SETTINGS,
                    value=requirements,
                    infer_from=infer_from(field)
                ))

        parse_dependencies(MetaNames.install_requires, 'dependencies')
        parse_dependencies(MetaNames.tests_require, 'dev-dependencies')

        def parse_extera():
            extras: dict = get_field(pyproject_data, 'tool.poetry.extras')
            if extras and isinstance(extras, dict):
                rv = {}
                dependencies = {}
                dependencies.update(get_field(pyproject_data, 'tool.poetry.dependencies') or {})
                dependencies.update(get_field(pyproject_data, 'tool.poetry.dev-dependencies') or {})
                requirements = get_requirements(dependencies, True)
                for extra, pkgs in extras.items():
                    if pkgs and isinstance(pkgs, list):
                        rv[extra] = {}
                        for pkg in pkgs:
                            rv[extra][pkg] = requirements.get(pkg) or Requirement(pkg)
                if rv:
                    context.set_result(MetaNames.extras_require, Metadata(
                        priority=Priorities.IMPLICIT_SETTINGS,
                        value=rv,
                        infer_from=infer_from('tool.poetry.extras')
                    ))
                    return rv

        parse_extera()

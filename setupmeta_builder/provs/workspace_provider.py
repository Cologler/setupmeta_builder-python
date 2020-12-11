# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import os

from packaging.requirements import Requirement

from ..consts import *
from ..abc import *
from ..bases import LongDescription
from ..helper import get_package_locations

SEARCH_PACKAGE_DIRS = ['', 'src']

@exported
class WorkspacePackagesProvider(IMetadataProvider):
    def get_provided(self) -> List[str]:
        return [MetaNames.packages, MetaNames.py_modules, MetaNames.package_dir]

    def get_dependencies(self) -> Union[List[str], str]:
        return [MetaNames.package_dir]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        def found(name: str, packages: List[str], infer_from: str, package_dir = None):
            context.set_result(name, Metadata(
                priority=Priorities.INFER,
                value=sorted(packages),
                infer_from=infer_from
            ))
            if package_dir:
                context.set_result(MetaNames.package_dir, Metadata(
                    priority=Priorities.INFER,
                    value=package_dir,
                    infer_from=infer_from
                ))
            return True

        from setuptools import find_packages

        root_dir = str(context.project.root_dir.path)

        def get_search_module_names():
            proj_name = str(context.project.root_dir.path.name)
            search_module_names = []
            search_module_names.append(proj_name)
            search_module_names.append(proj_name.replace('-', '_'))
            if proj_name.startswith('python-'):
                search_module_names.append(proj_name[len('python-'):])
            if proj_name.endswith('-python'):
                search_module_names.append(proj_name[:-len('-python')])
            return search_module_names

        def find_packages_from(package_dir: str, package_name: str):
            src_dir = os.path.join(root_dir, package_dir) if package_dir else root_dir
            packages = find_packages(where=root_dir, exclude=EXCLUDED_PACKAGES)
            if packages:
                package_dir_args = None
                if package_dir:
                    package_dir_args = {
                        package_name or '': package_dir
                    }
                return found(MetaNames.packages, packages, f'find_packages({src_dir})', package_dir=package_dir_args)

        def find_modules_from(package_dir: str, package_name: str):
            src_dir = os.path.join(root_dir, package_dir) if package_dir else root_dir
            for name in get_search_module_names():
                path = os.path.join(src_dir, f'{name}.py')
                if os.path.isfile(os.path.join(src_dir, f'{name}.py')):
                    package_dir_args = None
                    if package_dir:
                        package_dir_args = {
                            package_name or '': package_dir
                        }
                    return found(MetaNames.py_modules, [name], f'file <{path}>', package_dir=package_dir_args)

        dep_package_dirs = deps[MetaNames.package_dir]
        if dep_package_dirs:
            dpd = dep_package_dirs[0]
            for r1, r2 in dpd.value.items():
                if find_packages_from(r2, r1):
                    return
            for r1, r2 in dpd.value.items():
                if find_modules_from(r2, r1):
                    return
        else:
            for name in SEARCH_PACKAGE_DIRS:
                if find_packages_from(name, ''):
                    return
            for name in SEARCH_PACKAGE_DIRS:
                if find_modules_from(name, ''):
                    return


@exported
class WorkspacePackageNameProvider(IMetadataProvider):
    def get_provided(self) -> List[str]:
        return [MetaNames.name]

    def get_dependencies(self) -> Union[List[str], str]:
        return [MetaNames.packages, MetaNames.py_modules]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        if deps[MetaNames.packages]:
            packages: List[str] = deps[MetaNames.packages][0].value
            if packages:
                namespaces = list({p.partition('.')[0] for p in packages})
                if len(namespaces) > 1:
                    context.logger.warning(f'found multi root packages: {namespaces}')
                name = namespaces[0]
                context.set_result(MetaNames.name, Metadata(
                    priority=Priorities.INFER,
                    value=name,
                    infer_from=f'packages metadata'
                ))
                return

        if deps[MetaNames.py_modules]:
            modules: List[str] = deps[MetaNames.py_modules][0].value
            if modules:
                name = modules[0]
                context.set_result(MetaNames.name, Metadata(
                    priority=Priorities.INFER,
                    value=name,
                    infer_from=f'py_modules metadata'
                ))
                return


@exported
class WorkspaceRequirementsProvider(IMetadataProvider):
    def get_provided(self) -> List[str]:
        return [MetaNames.install_requires]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        requirements_text = context.project.read_text('requirements.txt')
        if not requirements_text:
            return
        requirements = [Requirement(l) for l in requirements_text.splitlines() if l]
        context.set_result(MetaNames.install_requires, Metadata(
            priority=Priorities.IMPLICIT_SETTINGS,
            value={r.name: r for r in requirements},
            infer_from='file <requirements.txt>'
        ))


@exported
class WorkspaceReadmeProvider(IMetadataProvider):
    def get_provided(self) -> List[str]:
        return [MetaNames.long_description]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):

        def find(name: str, content_type: str):
            content = context.project.read_text(name)
            if content is not None:
                context.set_result(MetaNames.long_description, Metadata(
                    priority=Priorities.INFER,
                    value=LongDescription(
                        long_description=content,
                        long_description_content_type=content_type
                    ),
                    infer_from=f'file <{name}>'
                ))
                return True

        if find('README.rst', 'text/x-rst') or find('README.md', 'text/markdown'):
            return
        if find('README.txt', 'text/plain') or find('README', 'text/plain'):
            return


@exported
class WorkspaceConsoleScriptsProvider(IMetadataProvider):
    def get_provided(self) -> List[str]:
        return [MetaNames.entry_points]

    def get_dependencies(self) -> Union[List[str], str]:
        return [MetaNames.packages, MetaNames.package_dir]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        packages = deps[MetaNames.packages]
        if not packages:
            return

        for pkg_name, pkg_location in get_package_locations(deps).items():
            path = os.path.join(pkg_location, 'entry_points_console_scripts.py')
            scripts = context.project.read_text(path)
            if scripts is not None:
                import ast
                fns = []
                mod = ast.parse(scripts)
                for stmt in mod.body:
                    if isinstance(stmt, ast.FunctionDef):
                        fns.append(stmt.name)

                console_scripts = {}
                for fn in fns:
                    if not fn.startswith('_'):
                        script_name = fn.replace('_', '-')
                        console_scripts[script_name] = f'{pkg_name}.entry_points_console_scripts:{fn}'

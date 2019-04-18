# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import abstractmethod, ABC

class RequiresResolver(ABC):
    @abstractmethod
    def resolve_install_requires(self, ctx) -> list:
        raise NotImplementedError

    @abstractmethod
    def resolve_tests_require(self, ctx) -> list:
        raise NotImplementedError

    def _sorted_list(self, ls):
        return list(sorted(ls))


class RequirementsTxtRequiresResolver(RequiresResolver):
    def resolve_install_requires(self, ctx) -> list:
        requirements = ctx.get_text_content('requirements.txt')
        if requirements is None:
            return None

        return self._sorted_list([l for l in requirements.splitlines() if l])

    def resolve_tests_require(self, ctx) -> list:
        return None


class PipfileRequiresResolver(RequiresResolver):
    def _get_pipfile(self, ctx):
        if 'pipfile' not in ctx.state:
            pipfile_path = ctx.root_path / 'Pipfile'
            if pipfile_path.is_file():
                import pipfile
                pf = pipfile.load(str(pipfile_path))
            else:
                pf = None
            ctx.state['pipfile'] = pf
        return ctx.state['pipfile']

    def _pipenv_package_to_require(self, k, v):
        if v == '*':
            return k
        raise NotImplementedError((k, v))

    def _resolve_requires(self, ctx, attr_name, pf_key):
        pf = self._get_pipfile(ctx)
        if pf is None:
            return None
        requires = []
        for k, v in pf.data[pf_key].items():
            requires.append(self._pipenv_package_to_require(k, v))
        return self._sorted_list(requires)

    def resolve_install_requires(self, ctx) -> list:
        return self._resolve_requires(ctx, 'install_requires', 'default')

    def resolve_tests_require(self, ctx) -> list:
        return self._resolve_requires(ctx, 'tests_require', 'develop')


class ChainRequiresResolver(RequiresResolver):
    def __init__(self, *resolvers):
        self.resolvers = list(resolvers)

    def resolve_install_requires(self, ctx) -> list:
        for r in self.resolvers:
            ret = r.resolve_install_requires(ctx)
            if ret is not None:
                return ret

    def resolve_tests_require(self, ctx) -> list:
        for r in self.resolvers:
            ret = r.resolve_tests_require(ctx)
            if ret is not None:
                return ret


class StrictRequiresResolver(RequiresResolver):
    def __init__(self, *resolvers):
        self.resolvers = list(resolvers)

    def _get_result(self, rets: list):
        rets = [r for r in rets if r is not None]
        if not rets:
            return None
        ret = rets[0]
        for o in rets[1:]:
            if o != ret:
                raise RuntimeError('different requires from multi source')
        return ret

    def resolve_install_requires(self, ctx) -> list:
        rets = [r.resolve_install_requires(ctx) for r in self.resolvers]
        return self._get_result(rets)

    def resolve_tests_require(self, ctx) -> list:
        rets = [r.resolve_tests_require(ctx) for r in self.resolvers]
        return self._get_result(rets)


class DefaultRequiresResolver(RequiresResolver):
    def __init__(self):
        self._install_resolver = StrictRequiresResolver(
            RequirementsTxtRequiresResolver(),
            PipfileRequiresResolver()
        )
        self._test_resolver = StrictRequiresResolver(
            PipfileRequiresResolver()
        )

    def resolve_install_requires(self, ctx) -> list:
        return self._install_resolver.resolve_install_requires(ctx)

    def resolve_tests_require(self, ctx) -> list:
        return self._test_resolver.resolve_tests_require(ctx)

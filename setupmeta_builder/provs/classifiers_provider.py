# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..consts import *
from ..abc import *
from ..utils import parse_version

from ..consts_classifiers import *

@exported
class DevelopmentStatusClassifiersProvider(IMetadataProvider):
    CLASSIFIER_PLANNING = 'Development Status :: 1 - Planning'
    CLASSIFIER_PRE_ALPHA = 'Development Status :: 2 - Pre-Alpha'
    CLASSIFIER_ALPHA = 'Development Status :: 3 - Alpha'
    CLASSIFIER_BETA = 'Development Status :: 4 - Beta'
    CLASSIFIER_STABLE = 'Development Status :: 5 - Production/Stable'
    CLASSIFIER_MATURE = 'Development Status :: 6 - Mature'
    CLASSIFIER_INACTIVE = 'Development Status :: 7 - Inactive'

    def get_provided(self) -> Union[List[str], str]:
        return MetaNames.classifiers

    def get_dependencies(self) -> Union[List[str], str]:
        return MetaNames.version

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        versions = deps[MetaNames.version]
        if versions:
            version = parse_version(versions[0].value)
            if version is not None:
                version_classifier: str = None
                if version.is_devrelease:
                    version_classifier = self.CLASSIFIER_PRE_ALPHA
                elif version.is_postrelease:
                    version_classifier = self.CLASSIFIER_ALPHA
                elif version.is_prerelease:
                    version_classifier = self.CLASSIFIER_BETA
                else:
                    version_classifier = self.CLASSIFIER_STABLE
                if version_classifier:
                    context.set_result(MetaNames.classifiers, Metadata(
                        priority=Priorities.INFER,
                        value=version_classifier,
                        infer_from='version metadata'
                    ))


@exported
class LicenseClassifiersProvider(IMetadataProvider):

    def get_provided(self) -> Union[List[str], str]:
        return [MetaNames.classifiers, MetaNames.license]

    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        # The license argument doesn’t have to indicate the license under which your package is being released,
        # although you may optionally do so if you want.
        # If you’re using a standard, well-known license,
        # then your main indication can and should be via the classifiers argument.

        def find_classifier(name: str):
            license_text = context.project.read_text(name)
            if license_text:
                header = license_text.strip().splitlines()[0]
                for li in LICENSE_CLASSIFIERS_TABLE:
                    for search_text in li.search_texts:
                        if search_text in header:
                            context.set_result(MetaNames.classifiers, Metadata(
                                priority=Priorities.INFER,
                                value=li.classifier,
                                infer_from=f'file <{name}>'
                            ))
                            return True

        def find_license(name: str):
            license_text = context.project.read_text(name)
            if license_text:
                header = license_text.strip().splitlines()[0]
                if header:
                    context.set_result(MetaNames.license, Metadata(
                        priority=Priorities.INFER,
                        value=header,
                        infer_from=f'file <{name}>'
                    ))
                    return True

        if find_classifier('LICENSE') or find_classifier('LICENSE.txt'):
            return
        else:
            find_license('LICENSE') or find_license('LICENSE.txt')

# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from dataclasses import dataclass

@dataclass
class LicenseInfo:
    classifier: str
    search_texts: List[str]
    spdx_id: Optional[str] = None


LICENSE_CLASSIFIERS_TABLE = [
    LicenseInfo(classifier='License :: Aladdin Free Public License (AFPL)',
                search_texts=['Aladdin Free Public License (AFPL)']),
    LicenseInfo(classifier='License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                search_texts=['CC0 1.0 Universal (CC0 1.0) Public Domain Dedication']),
    LicenseInfo(classifier='License :: CeCILL-B Free Software License Agreement (CECILL-B)',
                search_texts=['CeCILL-B Free Software License Agreement (CECILL-B)']),
    LicenseInfo(classifier='License :: CeCILL-C Free Software License Agreement (CECILL-C)',
                search_texts=['CeCILL-C Free Software License Agreement (CECILL-C)']),
    LicenseInfo(classifier='License :: DFSG approved',
                search_texts=['DFSG approved']),
    LicenseInfo(classifier='License :: Eiffel Forum License (EFL)',
                search_texts=['Eiffel Forum License (EFL)']),
    LicenseInfo(classifier='License :: Free For Educational Use',
                search_texts=['Free For Educational Use']),
    LicenseInfo(classifier='License :: Free For Home Use',
                search_texts=['Free For Home Use']),
    LicenseInfo(classifier='License :: Free To Use But Restricted',
                search_texts=['Free To Use But Restricted']),
    LicenseInfo(classifier='License :: Free for non-commercial use',
                search_texts=['Free for non-commercial use']),
    LicenseInfo(classifier='License :: Freely Distributable',
                search_texts=['Freely Distributable']),
    LicenseInfo(classifier='License :: Freeware',
                search_texts=['Freeware']),
    LicenseInfo(classifier='License :: GUST Font License 1.0',
                search_texts=['GUST Font License 1.0']),
    LicenseInfo(classifier='License :: GUST Font License 2006-09-30',
                search_texts=['GUST Font License 2006-09-30']),
    LicenseInfo(classifier='License :: Netscape Public License (NPL)',
                search_texts=['Netscape Public License (NPL)']),
    LicenseInfo(classifier='License :: Nokia Open Source License (NOKOS)',
                search_texts=['Nokia Open Source License (NOKOS)']),
    LicenseInfo(classifier='License :: OSI Approved',
                search_texts=['OSI Approved']),
    LicenseInfo(classifier='License :: OSI Approved :: Academic Free License (AFL)',
                search_texts=['Academic Free License (AFL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Apache Software License',
                spdx_id='Apache-2.0',
                search_texts=['Apache Software License']),
    LicenseInfo(classifier='License :: OSI Approved :: Apple Public Source License',
                search_texts=['Apple Public Source License']),
    LicenseInfo(classifier='License :: OSI Approved :: Artistic License',
                search_texts=['Artistic License']),
    LicenseInfo(classifier='License :: OSI Approved :: Attribution Assurance License',
                search_texts=['Attribution Assurance License']),
    LicenseInfo(classifier='License :: OSI Approved :: BSD License',
                search_texts=['BSD License']),
    LicenseInfo(classifier='License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
                search_texts=['Boost Software License 1.0 (BSL-1.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
                search_texts=['CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)']),
    LicenseInfo(classifier='License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)',
                search_texts=['Common Development and Distribution License 1.0 (CDDL-1.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: Common Public License',
                search_texts=['Common Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)',
                search_texts=['Eclipse Public License 1.0 (EPL-1.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)',
                search_texts=['Eclipse Public License 2.0 (EPL-2.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: Eiffel Forum License',
                search_texts=['Eiffel Forum License']),
    LicenseInfo(classifier='License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)',
                search_texts=['European Union Public Licence 1.0 (EUPL 1.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)',
                search_texts=['European Union Public Licence 1.1 (EUPL 1.1)']),
    LicenseInfo(classifier='License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
                search_texts=['European Union Public Licence 1.2 (EUPL 1.2)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Affero General Public License v3',
                search_texts=['GNU Affero General Public License v3']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                search_texts=['GNU Affero General Public License v3 or later (AGPLv3+)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Free Documentation License (FDL)',
                search_texts=['GNU Free Documentation License (FDL)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU General Public License (GPL)',
                search_texts=['GNU General Public License (GPL)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                spdx_id='GPL-2.0-only',
                search_texts=['GNU General Public License v2 (GPLv2)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                spdx_id='GPL-2.0-or-later',
                search_texts=['GNU General Public License v2 or later (GPLv2+)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                spdx_id='GPL-3.0-only',
                search_texts=['GNU General Public License v3 (GPLv3)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                spdx_id='GPL-3.0-or-later',
                search_texts=['GNU General Public License v3 or later (GPLv3+)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
                search_texts=['GNU Lesser General Public License v2 (LGPLv2)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
                search_texts=['GNU Lesser General Public License v2 or later (LGPLv2+)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                spdx_id='LGPL-3.0-only',
                search_texts=['GNU Lesser General Public License v3 (LGPLv3)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
                spdx_id='LGPL-3.0-or-later',
                search_texts=['GNU Lesser General Public License v3 or later (LGPLv3+)']),
    LicenseInfo(classifier='License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                search_texts=['GNU Library or Lesser General Public License (LGPL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)',
                search_texts=['Historical Permission Notice and Disclaimer (HPND)']),
    LicenseInfo(classifier='License :: OSI Approved :: IBM Public License',
                search_texts=['IBM Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: ISC License (ISCL)',
                search_texts=['ISC License (ISCL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Intel Open Source License',
                search_texts=['Intel Open Source License']),
    LicenseInfo(classifier='License :: OSI Approved :: Jabber Open Source License',
                search_texts=['Jabber Open Source License']),
    LicenseInfo(classifier='License :: OSI Approved :: MIT License',
                spdx_id='MIT',
                search_texts=['MIT License']),
    LicenseInfo(classifier='License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)',
                search_texts=['MITRE Collaborative Virtual Workspace License (CVW)']),
    LicenseInfo(classifier='License :: OSI Approved :: MirOS License (MirOS)',
                search_texts=['MirOS License (MirOS)']),
    LicenseInfo(classifier='License :: OSI Approved :: Motosoto License',
                search_texts=['Motosoto License']),
    LicenseInfo(classifier='License :: OSI Approved :: Mozilla Public License 1.0 (MPL)',
                search_texts=['Mozilla Public License 1.0 (MPL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
                search_texts=['Mozilla Public License 1.1 (MPL 1.1)']),
    LicenseInfo(classifier='License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                search_texts=['Mozilla Public License 2.0 (MPL 2.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: Nethack General Public License',
                search_texts=['Nethack General Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: Nokia Open Source License',
                search_texts=['Nokia Open Source License']),
    LicenseInfo(classifier='License :: OSI Approved :: Open Group Test Suite License',
                search_texts=['Open Group Test Suite License']),
    LicenseInfo(classifier='License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)',
                search_texts=['Open Software License 3.0 (OSL-3.0)']),
    LicenseInfo(classifier='License :: OSI Approved :: PostgreSQL License',
                search_texts=['PostgreSQL License']),
    LicenseInfo(classifier='License :: OSI Approved :: Python License (CNRI Python License)',
                search_texts=['Python License (CNRI Python License)']),
    LicenseInfo(classifier='License :: OSI Approved :: Python Software Foundation License',
                search_texts=['Python Software Foundation License']),
    LicenseInfo(classifier='License :: OSI Approved :: Qt Public License (QPL)',
                search_texts=['Qt Public License (QPL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Ricoh Source Code Public License',
                search_texts=['Ricoh Source Code Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)',
                search_texts=['SIL Open Font License 1.1 (OFL-1.1)']),
    LicenseInfo(classifier='License :: OSI Approved :: Sleepycat License',
                search_texts=['Sleepycat License']),
    LicenseInfo(classifier='License :: OSI Approved :: Sun Industry Standards Source License (SISSL)',
                search_texts=['Sun Industry Standards Source License (SISSL)']),
    LicenseInfo(classifier='License :: OSI Approved :: Sun Public License',
                search_texts=['Sun Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: The Unlicense (Unlicense)',
                search_texts=['The Unlicense (Unlicense)']),
    LicenseInfo(classifier='License :: OSI Approved :: Universal Permissive License (UPL)',
                search_texts=['Universal Permissive License (UPL)']),
    LicenseInfo(classifier='License :: OSI Approved :: University of Illinois/NCSA Open Source License',
                search_texts=['University of Illinois/NCSA Open Source License']),
    LicenseInfo(classifier='License :: OSI Approved :: Vovida Software License 1.0',
                search_texts=['Vovida Software License 1.0']),
    LicenseInfo(classifier='License :: OSI Approved :: W3C License',
                search_texts=['W3C License']),
    LicenseInfo(classifier='License :: OSI Approved :: X.Net License',
                search_texts=['X.Net License']),
    LicenseInfo(classifier='License :: OSI Approved :: Zope Public License',
                search_texts=['Zope Public License']),
    LicenseInfo(classifier='License :: OSI Approved :: zlib/libpng License',
                search_texts=['zlib/libpng License']),
    LicenseInfo(classifier='License :: Other/Proprietary License',
                search_texts=['Other/Proprietary License']),
    LicenseInfo(classifier='License :: Public Domain',
                search_texts=['Public Domain']),
    LicenseInfo(classifier='License :: Repoze Public License',
                search_texts=['Repoze Public License']),
]


@dataclass
class PythonInfo:
    classifier: str
    short_name: Optional[str] = None


PYTHON_CLASSIFIERS_TABLE = [
    PythonInfo(classifier='Programming Language :: Python',
               short_name='Python'),

    PythonInfo(classifier='Programming Language :: Python :: 2',
               short_name='2'),

    PythonInfo(classifier='Programming Language :: Python :: 2 :: Only',
               short_name='==2'),

    PythonInfo(classifier='Programming Language :: Python :: 2.3',
               short_name='2.3'),

    PythonInfo(classifier='Programming Language :: Python :: 2.4',
               short_name='2.4'),

    PythonInfo(classifier='Programming Language :: Python :: 2.5',
               short_name='2.5'),

    PythonInfo(classifier='Programming Language :: Python :: 2.6',
               short_name='2.6'),

    PythonInfo(classifier='Programming Language :: Python :: 2.7',
               short_name='2.7'),

    PythonInfo(classifier='Programming Language :: Python :: 3',
               short_name='3'),

    PythonInfo(classifier='Programming Language :: Python :: 3 :: Only',
               short_name='==3'),

    PythonInfo(classifier='Programming Language :: Python :: 3.0',
               short_name='3.0'),

    PythonInfo(classifier='Programming Language :: Python :: 3.1',
               short_name='3.1'),

    PythonInfo(classifier='Programming Language :: Python :: 3.10',
               short_name='3.10'),

    PythonInfo(classifier='Programming Language :: Python :: 3.2',
               short_name='3.2'),

    PythonInfo(classifier='Programming Language :: Python :: 3.3',
               short_name='3.3'),

    PythonInfo(classifier='Programming Language :: Python :: 3.4',
               short_name='3.4'),

    PythonInfo(classifier='Programming Language :: Python :: 3.5',
               short_name='3.5'),

    PythonInfo(classifier='Programming Language :: Python :: 3.6',
               short_name='3.6'),

    PythonInfo(classifier='Programming Language :: Python :: 3.7',
               short_name='3.7'),

    PythonInfo(classifier='Programming Language :: Python :: 3.8',
               short_name='3.8'),

    PythonInfo(classifier='Programming Language :: Python :: 3.9',
               short_name='3.9'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: CPython',
               short_name='CPython'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: IronPython',
               short_name='IronPython'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: Jython',
               short_name='Jython'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: MicroPython',
               short_name='MicroPython'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: PyPy',
               short_name='PyPy'),

    PythonInfo(classifier='Programming Language :: Python :: Implementation :: Stackless',
               short_name='Stackless'),
]

assert len(PYTHON_CLASSIFIERS_TABLE) == len(set(x.short_name for x in PYTHON_CLASSIFIERS_TABLE))

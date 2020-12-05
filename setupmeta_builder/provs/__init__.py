# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import importlib

for name in os.listdir(os.path.dirname(__file__)):
    if name.endswith('.py') and not name.startswith('_'):
        importlib.import_module('.' + name[:-3], package=__name__)

_ = None # use for import

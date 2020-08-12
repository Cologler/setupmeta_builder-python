# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import sys
import traceback

def create_setuppy(rootdir):
    path = os.path.join(rootdir, 'setup.py')
    with open(path, 'wt', encoding='utf-8') as w:
        w.write('\n'.join([
            '# auto generated by setupmeta_builder',
            '',
            'from setupmeta_builder import setup_it',
            '',
            'setup_it()',
            '',
        ]))

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        create_setuppy((argv + [os.getcwd()])[1])
    except Exception: # pylint: disable=W0703
        traceback.print_exc()

if __name__ == '__main__':
    main()

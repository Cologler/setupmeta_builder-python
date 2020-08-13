# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import re

RE_AUTHORS = re.compile('^(?P<name>.+) <(?P<email>.+@.+)>$')

def parse_author(author: str) -> Tuple[str, str]:
    author = author.strip()
    match = RE_AUTHORS.match(author)
    if match:
        author_name, author_email = match.group('name'), match.group('email')
        return author_name, author_email
    return author, None

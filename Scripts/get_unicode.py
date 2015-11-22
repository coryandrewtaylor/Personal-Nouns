# -*- coding: utf-8 -*-
"""
Get list of personal nouns with untranslated Unicode characters,
then write them to an output file.
"""
import re

with open("../Data/nouns.txt", "r") as nouns:
    with open("../Data/unicode.txt", "w") as xunicode:
        for noun in nouns.readlines():
            if (re.search("\\\\\'\w{1,2}", noun)
            or re.search(r"\\x[a-z0-9]{1,2}", noun)):
                xunicode.write(noun)

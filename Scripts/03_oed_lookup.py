# -*- coding: utf-8 -*-
"""
oed_lookup.py

Reads through PersonalNouns.txt, calls the Oxford English Dictionary API
for each word. If the API call is successful, writes the XML output to
OED_output.txt. If unsuccessful, writes the word to OED_errors.txt.
"""

import os
from time import sleep

import requests

with open(r"..\PersonalNouns.txt","r") as txt:
    original_words = list(txt.readlines())

with open(r"..\Data\OED_output.txt","w") as oed:
    with open(r"..\Data\OED_errors.txt", "w") as error_output:
        for number, word in enumerate(original_words):
            print(str(number) + " (" + word[:-1] + ") : start")
            url = "http://www.oed.com/srupage?operation=searchRetrieve&query=cql.serverChoice+=+" + word[:-1] + "&maximumRecords=100&startRecord=1"
            output = requests.get(url).text
            try:
                # Write the returned XML in a <div>,
                # removing the XML declaration from it first.
                oed.write("<div>" + output[39:] + "</div>\n")
            except UnicodeEncodeError:
                error_output.write(word[:-1] + os.linesep)
            print(str(number) + " (" + word[:-1] + ") : complete")

            sleep(1)
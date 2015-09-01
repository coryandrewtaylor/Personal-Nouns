# -*- coding: utf-8 -*-
"""
Using split Webster's files,
create a list of nouns that refer to people.
"""

from bs4 import BeautifulSoup as bs
from lxml import etree
from StringIO import StringIO
from os import listdir
import re

def NounOut(file1, file2):
    """
    For each entry in Webster's, find all the nouns.
    Then, narrow them down based on certain phrases.
    Last, write each one to a new line in the out file.
    """
    regex_woman = re.compile("woman[^'s]")
    regex_man = re.compile("(; a|A|The|; the) man ")
    regex_one = re.compile("(; o| O)ne [<>\/\w]+ed")
    regex_person = re.compile("person[,;.]")
    htmlparser = etree.HTMLParser()
    
    with open(file1, "r") as webster:
        with open(file2, "a") as nouns:
            soup = bs(webster)
            entries = soup.find_all("div")
            str_entries = str(entries)
            
            for entry in str_entries.split("</div>, <div>"):
                entry = re.sub("<Xpage=.*>\r\n", "", entry)
                if "<tt>n." in entry:
                    sub_soup = bs(entry)
                    defs = str(sub_soup.find_all("def"))
                    tree = etree.parse(StringIO(entry), htmlparser)
                    
                    if ("One who" in defs
                    or "one who" in defs
                    or "native or inhabitant" in defs
                    or "descendant" in defs
                    or re.search(regex_woman, defs)
                    or re.search(regex_man, defs)
                    or re.search(regex_one, defs)
                    or re.search(regex_person, defs)):
                        hw = str(tree.xpath("//h1/text()"))
                        hw = re.sub(", ", "\n", hw)
                        nouns.write(hw[2:-2] + "\n")

files = listdir("./WebsterFiles")
noun_file = "./Data/nouns.txt"

n = open(noun_file, "w")
n.close()

for xfile in files:
    xfile = "./WebsterFiles/" + xfile
    NounOut(xfile, noun_file)

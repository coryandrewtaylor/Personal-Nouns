# -*- coding: utf-8 -*-
"""
Remove nouns with untranslated Unicode characters.
Clean out single and double quotes from the entries.
Filter out adjectives, adverbs, and abstract and scientific nouns 
based on endings and part-of-speech tagging.
Normalize the capitalization. Deduplicate and alphabetize the list.
"""
from nltk.corpus import wordnet as wn
import re

adjadv = re.compile("([ai]ble|ful|o{0,1}i(c|sh|d)|i[nv]e|ian|less|like|ous|ly|al|[^l]ing|ose)$")
vbpre = re.compile("^(re|dis|over|u[np]|mis|out)", re.IGNORECASE)
vbsuf = re.compile("(i[sz]e|e[dn]|ate|i{0,1}fy)$")
abstrnoun = re.compile("([s|t]{0,1}ion|ism|ity|ment|ness|age|[ae]nce|ship|ability|acy)$")
scinoun = re.compile("(itis|ane|toxin|y|meter|liter|scope|tome|[o|y]l|[o|e]ne|sis|um|ma|i[n|a])$")

with open("../Data/nouns.txt", "r") as nouns:
    with open("../PersonalNouns.txt", "w") as cleaned:
        entries = []
        cleaned.write("""List of personal nouns in the 1890 Webster's Unabridged Dictionary.
Assembled by Cory Taylor from Project Gutenberg's HTML edition of the dictionary:
http://www.gutenberg.org/ebooks/673

This is a preliminary version of the list, so please forgive any noise.
Please report inaccuracies by email to coryandrewtaylor [at] gmail [dot] com 
or submit a pull request on GitHub (https://github.com/coryandrewtaylor/Personal-Nouns).
\n\n
""")
        for noun in nouns.readlines():
            noun = re.sub("^u[\"|\']", "", noun)
            noun = re.sub("[\"|\']", "", noun)
            
            if not (re.search(adjadv, noun)
            or re.search(vbpre, noun)
            or re.search(vbsuf, noun)
            or re.search(abstrnoun, noun)
            or re.search(scinoun, noun)
            or re.search("(^-|-\n)", noun)
            or re.search("\d+", noun)
            or " " in noun
            or "." in noun):
                noun = str(noun)[:-1]
                tag = wn.synsets(noun)
                if tag:
                    tag = str(tag)
                    if noun.lower() + ".n." in tag and "_" not in tag:
                        entries.append(noun.lower())
                else:
                    entries.append(noun.lower())
        entries = list(set(entries))        
        for entry in sorted(entries):
            cleaned.write(entry + "\n")

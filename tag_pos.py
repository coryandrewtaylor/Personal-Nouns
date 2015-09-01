# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:12:05 2015

@author: cory
"""

from nltk.corpus import wordnet as wn

with open("./Data/cleaned_nouns.txt", "r") as cleaned:
    with open("./Data/tagged_and_nouned.txt", "w") as tagnoun:
        entries = []
        for noun in cleaned.readlines():
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
            tagnoun.write(entry + "\n")
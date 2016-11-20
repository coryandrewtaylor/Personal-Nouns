# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:54:59 2015

@author: Cory Taylor
"""

with open('../Data/cleaned_nouns.txt', 'r') as nouns:
    suffixes = []    
    full_words = nouns.readlines()
    for word in full_words:
        suffixes.append(word[:-3])
    print(suffixes)

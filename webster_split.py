# -*- coding: utf-8 -*-
"""
Script to split HTML file of Webster's dictionary 
into several smaller files to make processing easier.
"""

with open("pg673.txt", "r") as webster:
    contents = webster.read()
    n = 1
    for letter in contents.split("<centered><point26>"):
        filename = str(n) + ".txt"
        with open(filename, "w") as open_file:
            open_file.write(letter)
        n = n + 1

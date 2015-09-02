# Personal-Nouns
This project is a list of personal nouns assembled from the 1890 Webster's Unabridged Dictionary, along with the
Python code that I used to prepare it.

### What's a "personal noun"?
A "personal noun" is a less clunky--if nonstandard--term for a common noun that refers to a person or a group of people. 

### Why a list of nouns?
I assembled this list in order to help produce accurate social networks of minor literary characters in Greco-Roman 
biography, as the current state of the art is only really reliable for detecting major characters in books that short.
However, the list has clear applications elsewhere, especially in distant/macroanalytic studies of character and genre.

### How the programs work:
The workflow is replatively simple:
First, the (relatively large) file from Project Gutenberg is chunked into files that fit into memory. 
Then, using ```BeautifulSoup``` and ```lxml```, nouns are identified (using the proxy of "n." being 
the first two characters of each entry's part of speech). The words are then filtered based on certain phrases that 
indicate that they refer to people.

The resulting set of words is still quite noisy, so adjectives, adverbs, verbs, and abstract and scientific nouns are 
filtered out via a series of regular expressions and ```nltk```'s ```WordNet```library.

### Find an error?
While I've done my best to make sure that the list only contains nouns that refer to people, there are doubtless several
errors that remain. If you find any--whether lingering noise or omitted personal nouns--please let me know. You can email 
me corrections at coryandrewtaylor [at] gmail [dot] com, or simply submit a pull request with the changes.

### Project Goal
This project selects 30,796 paper titles from five domains of computer science in DBLP papers, builds word bags (vocabulary dictionary) accordingly. It aims to look for frequent patterns, closed patterns and max patterns and match frequent words with domains.

### Preprocess
Initial processing involves stop words removal, case conversion, lemmatization.

### Algorithm Application
* Latent Dirichlet Allocation - Generates 5 topic files from titles.txt file.

* Frequent Pattern Mining - Programming Apriori Algorithm to find frequent patterns from each of the 5 topic files.

* Closed Pattern Mining

* Max Pattern Mining

* Purity Mining - Combines pattern frequency and uniqueness.

-- Note that patterns are indexed in mining procedures and mapped back to words in map_pattern.py.

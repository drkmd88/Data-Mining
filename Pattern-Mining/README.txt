### Project Goal
This project selects 30,796 paper titles from five domains of computer science in DBLP papers.

### Preprocess
Initial processing involves stop words removal, case conversion, lemmatization.

### Algorithm Application
1. Latent Dirichlet Allocation
Generates 5 topic files from titles.txt file.

2. Frequent Pattern Mining: Apriori Algorithm.
Find frequent patterns from each of the 5 topic files.

3. Closed Pattern Mining

4. Max Pattern Mining

5. Purity Mining
Combines pattern frequency and uniqueness.

-- Note that patterns are indexed in mining procedures and mapped back to words in map_pattern.py.

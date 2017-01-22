# Generate a dictionary
import sys

with open('paper.txt','r') as fin:
     paper = fin.read().splitlines()

# title key is title number; title value is title text in string format
title={}
for line in paper:
     eachline=line.split('\t')
     title[eachline[0]]=eachline[1]
   
    
dicwords=set()    
for value in title.values():
     dicwords=dicwords|set(value.split(' '))
    
dicwords=filter(None,dicwords)
   
with open('vocab.txt','w') as fout:
     fout.write('\n'.join(dicwords))
      


# Tokenize plain text by dictionary

with open('title.txt','a') as titleout:
  for line in paper:
      eachline=line.split('\t') # eachline[1] is a string of words separated by space
      eachline_word=filter(None,eachline[1].split(' ')) # a list of words
      if len(eachline_word)>0:
        diccnt={dicwords.index(x):eachline_word.count(x) for x in eachline_word}
        cnt=len(diccnt) # unique words in a title; equivalent to length of diccnt
        pairlist=[':'.join(str(x) for x in diccnt.items()[j]) for j in range(cnt)]
        pairlist.sort()
        titleout.write(str(cnt)+' '+' '.join(pairlist)+'\n')

        

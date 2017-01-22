with open('vocab.txt','r') as dicwords:
    dicwords=dicwords.read().splitlines() # a list of words, matches words and index

# frequent
def freqwords(n):
    with open('patterns\\pattern-'+str(n)+'.txt','r') as maxw:
        maxw=maxw.read().splitlines()
    with open('patterns\\pattern-'+str(n)+'.txt.pattern','a') as new:
        for line in maxw:
            maxspt=line.split(' ')
            val=maxspt[1:]
            valnew=[]
            for i in val:
                valnew+=[dicwords[int(i)]]
            new.write(maxspt[0]+' '+' '.join(valnew)+'\n')

# closed
def closewords(n):
    with open('closed\\closed-'+str(n)+'.txt','r') as maxw:
        maxw=maxw.read().splitlines()
    with open('closed\\closed-'+str(n)+'.txt.pattern','a') as new:
        for line in maxw:
            maxspt=line.split(' ')
            val=maxspt[1:]
            valnew=[]
            for i in val:
                valnew+=[dicwords[int(i)]]
            new.write(maxspt[0]+' '+' '.join(valnew)+'\n')

# max
def maxwords(n):
    with open('max\\max-'+str(n)+'.txt','r') as maxw:
        maxw=maxw.read().splitlines()
    with open('max\\max-'+str(n)+'.txt.pattern','a') as new:
        for line in maxw:
            maxspt=line.split(' ')
            val=maxspt[1:]
            valnew=[]
            for i in val:
                valnew+=[dicwords[int(i)]]
            new.write(maxspt[0]+' '+' '.join(valnew)+'\n')
            
def purewords(n):
    with open('purity\\purity-'+str(n)+'.txt','r') as maxw:
        maxw=maxw.read().splitlines()
    with open('purity\\purity-'+str(n)+'.txt.pattern','a') as new:
        for line in maxw:
            maxspt=line.split(' ')
            val=maxspt[1:]
            valnew=[]
            for i in val:
                valnew+=[dicwords[int(i)]]
            new.write(maxspt[0]+' '+' '.join(valnew)+'\n')
            

def main():
    for i in range(5):
        freqwords(i)
        closewords(i)
        maxwords(i)
        purewords(i)


if __name__ == '__main__':
	main()

# 0 machine learning, learning
# 1 theory
# 2 data mining: Most frequent word: data, mining,  data mining, frequent mining, pattern mining, 
# 3 information retrieval: Most frequent word: query, information, retrieval. Other characteristic: natural language, text, xml, term, file
# 4 database: Most frequent word: database, system, database system, relational, management. Other: dbms, schema, concurrency control, 
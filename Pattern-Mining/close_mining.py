import operator

def read_freq(file):
    with open(file,'r') as filein:
        filein=filein.read().splitlines()
    dicnew={}
    for line in filein:
        lineslt=line.split(' ')
        linekey=int(lineslt[0])
        lineval=[int(i) for i in lineslt[1:]]
        if linekey not in dicnew.keys():
            dicnew[linekey]=[lineval]
        else:
            dicnew[linekey]+=[lineval]
    return dicnew
    


def filter_one(process):
    '''
    If one support value has only one corresponding item, the item must be closed;
    Otherwise, if the support value has only one-item, those items must also be closed;
    '''
    dicone={}
    dictest={}
    for key,value in process.items():
        if len(value)==1 or max([len(i) for i in value])==1:
            dicone[key]=value
        else:
            dictest[key]=value
    return dicone,dictest
    
def filter_more(dic):
    '''
    dictest is input
    '''
    dicafter={}
    for key,tot in dic.items():
        valuenew=[]
        for value in tot: # list format, ie. [735,3468]
            if pattern_close(value,tot) is True:
                valuenew.append(value)
        dicafter[key]=valuenew
    return dicafter
    
def pattern_close(part,tot):
    '''
    tot is a list of lists; each list is part--which needs to be checked
    to see if they are subset of other part of the tot list
    '''
    for i in tot:
        if set(part).issubset(set(i)) and part!=i:
            return False
    return True                   
        

def out_format(dic,n):
    sortptn=sorted(dic.items(),key=operator.itemgetter(0),reverse=True) # turns a dictionary into a list of tuples
    with open('closed\\closed-'+str(n)+'.txt','a') as outfile:
        for i in sortptn:
            k=len(i[1])
            for j in range(k):
                dedelim=str(i[1][j]).strip('[]')
                outfile.write(str(i[0])+' '+' '.join(dedelim.split(', '))+'\n')

def comb_two(dic1,dic2,n):
    return out_format(dict(dic1.items()+dic2.items()),n)



def main():
    for i in range(5):
        f=read_freq('patterns\pattern-'+str(i)+'.txt')
        dicone,dictest=filter_one(f)
        dicafter=filter_more(dictest)
        comb_two(dicone,dicafter,i)


if __name__ == '__main__':
    main()
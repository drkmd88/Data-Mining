import operator

# first scan and get one-itemset
def wordbag(file):
    '''
    generate one-itemset and corresponding frequency
    generate n as number of item combinations
    '''
    bagw={}
    with open(file,'r') as top: # all appeared itemset:
        top=top.read().splitlines()
        for line in top:
            words=line.split(' ')
            for item in words:
              if tuple([item]) not in bagw.keys():
                  bagw[tuple([item])]=1
              else:
                  bagw[tuple([item])]+=1
    return bagw,len(top)
        

def prune(dic,supp):
    '''
    dic is a dictionary with item, frequency pair.
    return satisfactory pairs with frequency>=supp
    '''
    dicp={}
    dick=[key for key,value in dic.items() if value>=supp]
    for i in dick:
        dicp[i]=dic[i]
    return dicp
    
    
def getcomb(dic):
    '''
    calculate itemset from current frequent patterns
    '''
    keylist=[list(key) for key in dic.keys()]
    k=len(keylist)
    new=[]
    for i in range(k-1):
        ikey=keylist[i]
        ik=len(ikey)
        for j in range(i+1,k):
            jkey=keylist[j]
            for el in jkey:
                comb=set(ikey)|set([el])
                if len(comb)==ik+1 and comb not in new:
                    new.append(comb)
    new=[list(i) for i in new]
    return new
    

# scan dabaset again to get new n-itemset
def getitem(file,comp):
    '''
    generate frequencies for new patterns
    comp is a list of lists
    '''
    bagw={}
    for i in comp:
        bagw[tuple(i)]=0
        
    with open(file,'r') as top:
         for line in top:
             words=line.strip('\n').split(' ')
             for i in comp:
                 if set(i).issubset(words):
                     bagw[tuple(i)]+=1
    return bagw

def freq_item(file,psupp):
    bagw,n=wordbag(file) # scan dataset for the 1st time to get one-items and their counts in dictionary format
    base={}
    
    supp=psupp*n
    prunei=prune(bagw,supp) # filter frequency pairs
    
    while len(prunei)>=1:
        base.update(prunei)        # append to frequency pattern dictionary
        comb=getcomb(prunei)       # calculate itemsets from current frequent patterns
        bagwn=getitem(file,comb)   # generate frequencies for new patterns
        prunei=prune(bagwn,supp)
    return base
    
def get_pattern(freqitem,file):
    '''
    Organize frequent patterns in required format
    '''
    sortptn=sorted(freqitem.items(),key=operator.itemgetter(1),reverse=True)
    with open('patterns\\'+file,'a') as out:
        for i in sortptn:
            out.write(str(i[1])+' '+' '.join(i[0])+'\n')     



def main():
    for i in range(5):
        get_pattern(freq_item('topic-'+str(i)+'.txt',0.01),'pattern-'+str(i)+'.txt')
        print str(i)+ 'step finished'


if __name__ == '__main__':
    main() 


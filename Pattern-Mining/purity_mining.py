import math
import operator
import numpy as np

def read_freq2(n):
    with open('patterns\pattern-'+str(n)+'.txt','r') as filein:
      dic={}
      for line in filein:
          linespt=line.strip('\n').split(' ')
          dic[tuple(linespt[1:])]=int(linespt[0])
    return dic
    
def ftp(p,t):
    '''
    p is the pattern (in tuple format)
    t is the index of topic file
    returns the frequency of p in t
    '''
    ft=read_freq2(t)
    if p in ft.keys():
        fpt=ft[p]
    else:
        fpt=0
    return fpt

def getitem(comp,t):
    '''
    generate frequencies for new patterns
    '''
    bagw={}
    for i in comp:
        bagw[tuple(i)]=0
        
    with open('topic-'+str(t)+'.txt','r') as top:
         for line in top:
             words=line.strip('\n').split(' ')
             for i in comp:
                 if set(i).issubset(words):
                     bagw[tuple(i)]+=1
    return bagw
        
    
def dt(t):
    '''
    count the number of lines in file t
    '''
    with open('topic-'+str(t)+'.txt','r') as d:
        d=d.readlines()
    return len(d)
    
def turnlist(n):
    '''
    turn a file into a list of patterns
    '''
    with open('topic-'+str(n)+'.txt','r') as fn:
        fn=fn.read().splitlines()
        ln=[]
        for line in fn:
            ln.append(set(line.split()))
    return ln

def merget(a,b):
    '''
    union two topic files
    return D(file-a,file-b)
    '''
    fa=turnlist(a)
    fb=turnlist(b)
    lab=fa+fb
    fc=set(frozenset(i) for i in lab)
    return len([set(i) for i in fc])


def purity(p,a):
    '''
    calculate purity
    input: p is pattern; a is corresponding file number
    '''
    five=range(5)
    five.remove(a)
    compmax=range(4)
    ftpa=ftp(p,a)
    for b in range(4):
        compmax[b]=(ftpa+getitem([list(p)],five[b]).values()[0])/float(merget(a,five[b]))
    return round(math.log(float(ftpa)/dt(a),2)-math.log(max(compmax),2),4)


def allpurity(n):
    f=read_freq2(n)
    dic={}
    for i in f.keys():
        dic[i]=purity(i,n)
    return dic


def newstat(dic1,dic2):
    '''
    combine frequency and purity of a pattern to generate a new statistic
    '''
    newdic={}
    nu1=np.mean(dic1.values())
    sd1=np.std(dic1.values())
    nu2=np.mean(dic2.values())
    sd2=np.std(dic2.values())
    for key in dic1.keys():
        newdic[key]=(dic1[key]-nu1)/sd1+(dic2[key]-nu2)/sd2
    return newdic
    

def get_newstat(dic1,dic2,n):
    '''
    dic1 is pattern:frequency dictionary
    dic2 is pattern:purity dictionary
    '''
    newdic=newstat(dic1,dic2)
    sortptn=sorted(newdic.items(),key=operator.itemgetter(1),reverse=True) # sort dictionary key by newstat
    keyord=[i[0] for i in sortptn] # sorted pattern (key)
    sortnew=sorted(dic2.items(), key=lambda i:keyord.index(i[0]))
    
    with open('purity\\'+'purity-'+str(n)+'.txt','a') as out:
        for i in sortnew:
            out.write(str(i[1])+' '+' '.join(i[0])+'\n')
            
def main():
    for i in range(5):
        get_newstat(read_freq2(i),allpurity(i),i)


if __name__ == '__main__':
	main()
import operator

def read_freq2(n):
    with open('patterns\pattern-'+str(n)+'.txt','r') as filein:
      dic={}
      for line in filein:
          linespt=line.strip('\n').split(' ')
          dic[tuple(linespt[1:])]=int(linespt[0])
    return dic
    
def max_pattern(dic):
    m=max([len(i) for i in dic.keys()])
    rg=[i-j for i,j in zip([m]*m,range(m))][:-1]
    for k in rg:
        papool=[i for i in dic.keys() if len(i)==k]
        for elm in papool:
            for key in dic.keys():
                if set(key).issubset(elm) and key!=elm:
                    del dic[key]
    return dic

def out_format2(dic,n):
    sortptn=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
    with open('max\\'+'max-'+str(n)+'.txt','a') as out:
        for i in sortptn:
            out.write(str(i[1])+' '+' '.join(i[0])+'\n')


def main():
    for i in range(5):
        out_format2(max_pattern(read_freq2(i)),i)

if __name__ == '__main__':
    main()
    

    
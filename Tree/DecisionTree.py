import sys
import random


def readin(file):
    '''
    Organize data into a list of lists.
    The first element in each list is response while other elements are predictors
    '''
    with open(file,'r') as fin:
        fread = fin.read().splitlines()
    fsep = [i.split(' ') for i in fread] # separate the string into a list
    fout = []
    for i in fsep:
        if i!=['']:
            fout.append([int(i[0])] + [int(j.split(':')[1]) for j in i[1:]])
    return fout
        

def sepdata(dataset, col, value):
    '''
    separate a dataset according to certain value of a column
    '''
    set1 = [row for row in dataset if row[col] == value]
    set2 = [row for row in dataset if not row[col] == value]
    return set1, set2


def classcnt(dataset):
    '''
    calculate count of a class in dataset
    '''
    classcnt = {}
    for row in dataset:
        key = row[0]
        if key not in classcnt:
            classcnt[key] = 1
        else:
            classcnt[key] += 1
    return classcnt


def gini(dataset):
    '''
    calculate gini index of dataset D
    '''
    gini = 1.0
    n = len(dataset)
    psquare = [(float(row)/n)**2 for row in classcnt(dataset).values()]
    return gini-sum(psquare)


def comb(dataset):
    '''
    Key, value pairs of columns and values they can take
    '''
    k = len(dataset[0])-1
    comb = {}
    for i in range(k):
        comb[i+1] = list(set([l[i+1] for l in dataset]))
    return comb


class decisiontree(object):
    def __init__(self, col = -1, val = None, result = None, yt = None, nt = None):
        self.col = col # column index
        self.val = val # value of column that generates true result
        self.result = result
        self.yt = yt # yes subtree
        self.nt = nt # no subtree


def growtree(dataset):
    '''
    Choose split column and value based on maximum impurity reduction of gini index.
    At leaf node, apply majority vote mechanism to specify class;
    For equal votes, randomly assign class.
    '''
    if len(dataset)==0:
        return decisiontree()

    opt_reduce = 0.0
    opt_criteria = None
    opt_set = None
    
    combtry = comb(dataset) # variables and their values in dictionary format

    # calculate impurity_reduction using gini index
    giniD = gini(dataset)
    n = len(dataset)

    for col in combtry.keys():
        for val in combtry[col]:
            set1, set2 = sepdata(dataset, col, val)
            giniAD = float(len(set1))/n*gini(set1) + float(len(set2))/n*gini(set2)
            each_reduce = giniD - giniAD
            if  each_reduce > opt_reduce and len(set1)>0 and len(set2)>0:
                opt_reduce = each_reduce
                opt_criteria = (col, val)
                opt_set = (set1,set2)

    # create sub branches
    if opt_reduce > 0:     # Should there be impurity reduction, further split nodes.
        ysubtree = growtree(opt_set[0])
        nsubtree = growtree(opt_set[1])
        return decisiontree(col = opt_criteria[0], val = opt_criteria[1], yt = ysubtree, nt = nsubtree)

    else:   # If there's no impurity reductionuse, use majority vote to leave one terminal node only one class.
        leafcnt = classcnt(dataset)
        majoritycnt = {key:value for (key,value) in leafcnt.items() if value == max(leafcnt.values())}
        if len(majoritycnt) == 1:
            return decisiontree(result = majoritycnt)
        else:
            oneclass = random.choice(majoritycnt.keys()) # randomly assign class if equal vote
            return decisiontree(result = {oneclass:majoritycnt[oneclass]})


def showtree(tree, indent = ' '):
    if tree.result != None:
        return str(tree.result)
    else:
        return str(tree.col) + ':' + str(tree.val) + '?' + '\n'  + indent + 'Yes->' + ' ' + \
        showtree(tree.yt, indent +'  ') + '\n'  + indent + ' No->' + ' ' + \
        showtree(tree.nt, indent +'  ') 


def classnew(obs, tree):
    '''
    input obs is a list of predictors
    output is a list element of class
    '''
    if tree.result != None:
        return tree.result.keys()
    else:
        addto = None
        if obs[tree.col-1] == tree.val:
            addto = tree.yt
        else:
            addto = tree.nt
    return classnew(obs,addto)


def testresult(ntest, tree):
    predictors = [i[1:] for i in ntest]
    predtest = [classnew(i, tree)[0] for i in predictors]
    return predtest



def conf_matrix(ntrain, ntest, predtest):
    truetest = [i[0] for i in ntest]
    traintest = [i[0] for i in ntrain]
    allval = list(set(truetest).union(set(predtest)).union(set(traintest)))
    k = len(allval)
    confm = [[0 for i in range(k)] for j in range(k)]

    for i in range(k):
        for j in range(k):
            for elm in range(len(truetest)):
                if truetest[elm]==allval[i] and predtest[elm]==allval[j]:
                    confm[i][j] += 1
    return confm
            

def main():
    ntrain = readin(sys.argv[1])
    ntest = readin(sys.argv[2])
    predtest = testresult(ntest, growtree(ntrain))
    confm = conf_matrix(ntrain, ntest, predtest)
    finalout = ''
    for i in confm:
        finalout += ' '.join(str(j) for j in i) + '\n'
    print finalout



if __name__ == '__main__':
    main()   

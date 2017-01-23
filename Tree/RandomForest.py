import sys
import math
import random
import operator
import DecisionTree
import RandomForest


def combrand(dataset):
    k = len(dataset[0])-1
    # randk = random.sample(range(k), k/3+1)
    randk = random.sample(range(k),int(math.sqrt(k)))
    # randk = random.sample(range(k),k-1)
    comb = {}
    for i in randk:
        comb[i+1] = list(set([l[i+1] for l in dataset]))
    return comb


# def boot(dataset, prob):
#     '''
#     Bootstrap: Randomly select the proportion of samples as training data for each tree
#     '''
#     n = len(dataset)
#     return random.sample(dataset, int(n*prob))


def bootstrap(dataset):
    ''' Sample with replacement'''
    n = len(dataset)
    getwith = []
    for i in range(n):
        getwith += random.sample(dataset, 1)
    return getwith
    
     
def growparttree(subdata):
    '''
    Step1: Randomly select number of variables in each split where k is the number of attributes;
    Step2: Generate decision tree;
    Note the input data should be subset of the whole dataset.
    '''

    opt_reduce = 0.0
    opt_criteria = None
    opt_set = None
        
    
    combtry = combrand(subdata) # variables and their values in dictionary format

    # calculate impurity_reduction using gini index
    giniD = DecisionTree.gini(subdata)
    n = len(subdata)

    for col in combtry.keys():
        for val in combtry[col]:
            set1, set2 = DecisionTree.sepdata(subdata, col, val)
            giniAD = float(len(set1))/n*DecisionTree.gini(set1) + float(len(set2))/n*DecisionTree.gini(set2)
            each_reduce = giniD - giniAD
            if  each_reduce > opt_reduce and len(set1)>0 and len(set2)>0:
                opt_reduce = each_reduce
                opt_criteria = (col, val)
                opt_set = (set1,set2)

    # create sub branches
    if opt_reduce > 0:     # Should there be impurity reduction, further split nodes.
        ysubtree = growparttree(opt_set[0])
        nsubtree = growparttree(opt_set[1])
        return DecisionTree.decisiontree(col = opt_criteria[0], val = opt_criteria[1], yt = ysubtree, nt = nsubtree)

    else:   # If there's no impurity reduction, use majority vote to leave one terminal node only one class.
        leafcnt = DecisionTree.classcnt(subdata)
        majoritycnt = {key:value for (key,value) in leafcnt.items() if value == max(leafcnt.values())}
        if len(majoritycnt) == 1:
            return DecisionTree.decisiontree(result = majoritycnt)
        else:
            oneclass = random.choice(majoritycnt.keys()) # randomly assign class if equal vote
            return DecisionTree.decisiontree(result = {oneclass:majoritycnt[oneclass]})



def rf(ntrain, ntest, num):
    k = len(ntest)
    predtest_all = []
    for e in range(k):
        predtest_all.append({})
        
    for i in range(num):
        pred_part = DecisionTree.testresult(ntest, growparttree(bootstrap(ntrain)))
        for j in range(k):
            key = pred_part[j]
            if key in predtest_all[j].keys():
                predtest_all[j][key] += 1
            else:
                predtest_all[j][key] = 1

	predfinal = []
	for elm in predtest_all:
          pred = max(elm.iteritems(), key = operator.itemgetter(1))[0]
          predfinal.append(pred)
    return predfinal

 
def main():
    ntrain = DecisionTree.readin(sys.argv[1])
    ntest = DecisionTree.readin(sys.argv[2])
    predtest = rf(ntrain, ntest, 150)
    confm = DecisionTree.conf_matrix(ntrain, ntest, predtest)
    finalout = ''
    for i in confm:
        finalout += ' '.join(str(j) for j in i) + '\n'
    print finalout



if __name__ == '__main__':
	main()
 

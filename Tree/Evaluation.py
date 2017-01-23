import sys
import DecisionTree
import RandomForest

class Evaluation(object):

	def __init__(self, confmatrix, i):
		self.confmatrix = confmatrix
		self.k = len(confmatrix)
		self.i = i # i is class label

		self.TP = confmatrix[i][i]
		self.FN = sum([j for j in confmatrix[i] if j!=confmatrix[i][i]])
		self.FP = sum([confmatrix[j][i] for j in range(self.k) if j!=i])
	 	self.TN = sum([confmatrix[m][m] for m in range(self.k) if m!=i])


	def sensitivity(self):
		if (self.TP+self.FN)!=0:
			return float(self.TP)/(self.TP+self.FN)
		else:
			return 0

	def specificity(self):
		if (self.TN+self.FP)!=0:
			return float(self.TN)/(self.TN+self.FP)
		else:
			return 0

	def precision(self):
		if (self.TP+self.FP)!=0:
			return float(self.TP)/(self.TP+self.FP)
		else:
			return 0

	def recall(self):
	 	return self.sensitivity()

	def Fmeasure(self, b1, b2):
		P = self.precision()
		R = self.recall()
		AllF = []
		PR = P*R

		if P==0 and R==0:
			AllF += [0,0,0]
			return AllF
		else:
			AllF.append(float(2*PR/(P+R)))
			b1sq = pow(b1,2)
			b2sq = pow(b2,2)

			AllF.append(float((b1sq+1)*PR)/(b1sq*P+R))
			AllF.append(float((b2sq+1)*PR)/(b2sq*P+R))
		return AllF



def prtresult(classiname, confmx):
	print classiname
	print "-------------------------"
	finalout = ''
	print "Confusion Matrix: "
	AllTrue = 0

	for i in range(len(confmx)):
		finalout += ' '.join(str(j) for j in confmx[i]) + '\n'
		AllTrue += confmx[i][i]
	print finalout
	print "accuracy overall: " + str(float(AllTrue)/sum([sum(i) for i in confmx]))
	print ""

	for i in range(len(confmx)):
		confmatrix1=Evaluation(confmx,i)
		print "sensitivity of class " + str(i+1) + ": " + str(confmatrix1.sensitivity())
		print "specificity of class " + str(i+1) + ": " + str(confmatrix1.specificity())
		print "precision of class " + str(i+1) + ": " + str(confmatrix1.precision())
		print "recall of class " + str(i+1) + ": " + str(confmatrix1.recall())
		F = confmatrix1.Fmeasure(0.5,2)
		print "F1 of class " + str(i+1) + ": " + str(F[0])
		print "F-measure " + "beta=0.5 of class " + str(i+1) + ": " + str(F[1])
		print "F-measure " + "beta=2 of class " + str(i+1) + ": " + str(F[2])
		print ""


def main():
	ntrain = DecisionTree.readin(sys.argv[1])
	ntest = DecisionTree.readin(sys.argv[2])
	confmx = DecisionTree.conf_matrix(ntrain, ntest, DecisionTree.testresult(ntest, DecisionTree.growtree(ntrain)))
	confmxrf = DecisionTree.conf_matrix(ntrain, ntest, RandomForest.rf(ntrain, ntest, 100))
	prtresult("Decision Tree", confmx)
	prtresult("Random Forest", confmxrf)


if __name__ == '__main__':
	main()

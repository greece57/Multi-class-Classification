from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

def classify(trainSet, trainLabels, testSet):
	
	clf = LogisticRegression()
	clf.fit(trainSet, trainLabels)
	predictedLabels = clf.predict_proba(testSet)

	return predictedLabels, clf.classes_

def classifyBayes(trainSet, trainLabels, testSet):
    
    clf = GaussianNB()
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
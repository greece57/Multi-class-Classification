from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def classifyLogisticRegression(trainSet, trainLabels, testSet):
	
	clf = LogisticRegression()
	clf.fit(trainSet, trainLabels)
	predictedLabels = clf.predict_proba(testSet)

	return predictedLabels, clf.classes_

def classifyRandomForest(trainSet, trainLabels, testSet):
    
    clf = RandomForestClassifier(1000)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def classifyLogisticRegression(trainSet, trainLabels, testSet):
	
	clf = LogisticRegression(solver='lbfgs', multi_class='multinomial')
	clf.fit(trainSet, trainLabels)
	predictedLabels = clf.predict_proba(testSet)

	return predictedLabels, clf.classes_

def classifyRandomForest(trainSet, trainLabels, testSet):
    
    clf = RandomForestClassifier(1000, verbose=2, n_jobs=-1)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
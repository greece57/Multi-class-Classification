from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

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
    
def classifyRandomForest(trainSet, trainLabels, testSet):
    
    clf = RandomForestClassifier(100, min_samples_split=4, n_jobs=1)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
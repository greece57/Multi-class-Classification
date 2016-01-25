from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

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
    
    clf = RandomForestClassifier(1000, min_samples_split=4, verbose=10, n_jobs=4)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
    
def classifySupportVectorMaschine(trainSet, trainLables, testSet):
    
    clf = SVC(C=2.0, probability=True, verbose=True)
    clf.fit(trainSet, trainLables)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
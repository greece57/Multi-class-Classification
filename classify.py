from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
    
def classifyLogistic(trainSet, trainLabels, testSet):

    clf = LogisticRegression(C=0.4, solver='lbfgs', verbose=1, max_iter=10000, multi_class='multinomial')
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_

def classifyBayes(trainSet, trainLabels, testSet):
    
    clf = GaussianNB()
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
    
def classifyRandomForest(trainSet, trainLabels, testSet):
    
    clf = RandomForestClassifier(100, min_samples_split=4, verbose=10, n_jobs=1)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
    
def classifySupportVectorMaschine(trainSet, trainLabels, testSet):
    
    clf = SVC(C=2.0, probability=True, verbose=True)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
    
def classifyGradientBoosting(trainSet, trainLabels, testSet):
    
    clf = GradientBoostingClassifier(verbose=1)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_

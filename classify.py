from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
    
def classifyLogistic(trainSet, trainLabels, testSet):

    clf = LogisticRegression(C=0.4, solver='lbfgs', verbose=1, max_iter=10000, multi_class='multinomial', n_jobs=1)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_

def classifyBayes(trainSet, trainLabels, testSet):
    
    clf = GaussianNB()
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_
    
def classifyRandomForest(trainSet, trainLabels, testSet):
    
    clf = RandomForestClassifier(1000, min_samples_split=25, verbose=10, n_jobs=20)
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
    
def classifyDecisionTree(trainSet, trainLabels, testSet):
    
    clf = DecisionTreeClassifier(min_samples_split=500)
    clf.fit(trainSet, trainLabels)
    predictedLabels = clf.predict_proba(testSet)
    
    return predictedLabels, clf.classes_

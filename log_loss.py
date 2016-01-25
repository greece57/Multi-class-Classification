import numpy as np
from math import log
from sklearn.cross_validation import KFold
from joblib import Parallel, delayed


def calc(X,Y,classifier):
    kf = KFold(X.shape[0], n_folds=10) # Initialize cross validation

    loglosses = [] # Variable that will store the correctly predicted intances
    
    loglosses = Parallel(n_jobs=10, verbose=10)(delayed(innerLoopLogLoss)(trainIndex, testIndex, X, Y, classifier) for trainIndex, testIndex in kf)    
    
    totalLogloss = 0
    for logloss in loglosses:
        totalLogloss += logloss
    print 'Average Log Loss: ', totalLogloss/len(loglosses)
    return (totalLogloss/len(loglosses)), loglosses
    
def innerLoopLogLoss(trainIndex, testIndex, X, Y, classifier):
    
    
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = Y[trainIndex]

    predictions, trips = classifier(trainSet, trainLabels, testSet)
    
    testLabels = Y[testIndex]
    
    logloss = log_loss(testLabels, predictions, trips)
    strOutput = 'Logloss: ' + str(logloss)
    print strOutput
    return logloss
    
def log_loss(trueLabels, predictedLabels, trips, eps=1e-15):

    sums = predictedLabels.sum(axis=1)
    for i in range(predictedLabels.shape[0]):
        predictedLabels[i,:]/sums[i]

    predictedClippedLabels = np.clip(predictedLabels, eps, 1 - eps)

    logloss = 0	
    for i in range(trueLabels.size):
        logloss -= log(predictedClippedLabels[i,np.where(trips==trueLabels[i])[0][0]])	

    logloss /= trueLabels.size

    return logloss

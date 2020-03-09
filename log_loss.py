import numpy as np
import time
from math import log
from sklearn.model_selection import KFold
from classify import classifyRandomForest
from joblib import Parallel, delayed


def calcLogLoss(X,Y,classifier):
    kf = KFold(n_splits=10) # Initialize cross validation

    loglosses = [] # Variable that will store the correctly predicted intances
    
    # calculate Loglosses
    if (False):
        # execute 10 logloss calculations parallel
        loglosses = Parallel(n_jobs=10, verbose=10)(delayed(innerLoopLogLoss)(trainIndex, testIndex, X, Y, classifier) for trainIndex, testIndex in kf.split(X))    
    else:
        # only for random Forest
        # prints progress into progress file
        # and works parallel in the classifier because of n_job param
        idx = 0    
        for trainIndex, testIndex in kf.split(X):
            # calc 1 logLoss in the inner LogLoss-Loop
            logloss = innerLoopLogLoss(trainIndex, testIndex, X, Y, classifier)
            loglosses.append(logloss)
        
            # write progress into file
            idx+=1
            fw = open("progress", 'a')
            outputString = time.ctime() + " - " + str(idx) + ". Logloss: " + str(logloss) + "\n"
            print(outputString)
            fw.write(outputString)
            fw.close()
    
    
    # calc TotalLogLoss
    totalLogloss = 0
    for logloss in loglosses:
        totalLogloss += logloss
    print('Average Log Loss: ', totalLogloss/len(loglosses))
    
    return (totalLogloss/len(loglosses)), loglosses
    
def innerLoopLogLoss(trainIndex, testIndex, X, Y, classifier):
    # classifies given Set and calcs LogLoss
    
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = Y[trainIndex]

    predictions, trips = classifier(trainSet, trainLabels, testSet)
    
    testLabels = Y[testIndex]
    
    logloss = log_loss(testLabels, predictions, trips)
    strOutput = 'Logloss: ' + str(logloss)
    print(strOutput)
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

import numpy as np
import threading
import time
from math import log
from sklearn.cross_validation import KFold

iterations = 0 # Variable that will store the iterations
loglosses = [] # Variable that will store the correctly predicted intances  
lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, trainIndex, testIndex, X, Y, classifier):
        threading.Thread.__init__(self)
        self.trainIndex = trainIndex
        self.testIndex = testIndex
        self.X = X
        self.Y = Y
        self.classifier = classifier
        self.handled = False
    def run(self):
        innerLoopLogLoss(self.trainIndex, self.testIndex, self.X, self.Y, self.classifier)
        self.handled = True

def calc(X,Y,classifier,maxThreads):
    kf = KFold(X.shape[0], n_folds=10) # Initialize cross validation

    threads = []
    idx = 0
    activeThreads = 0
    for trainIndex, testIndex in kf:
        while (activeThreads >= maxThreads):
            time.sleep(2)
            activeThreads = countActiveThreads(threads)
            threads = [thread for thread in threads if not thread.handled]
        t = Thread(trainIndex, testIndex, X, Y, classifier)
        idx += 1
        print 'Starting Thread ', idx
        t.start()
        threads.append(t)
        threads = [thread for thread in threads if not thread.handled]
        activeThreads = countActiveThreads(threads)
    for thread in threads:
        thread.join()
    threads = [thread for thread in threads if not thread.handled]
        
    totalLogloss = 0
    for logloss in loglosses:
        totalLogloss += logloss
    print 'Average Log Loss: ', totalLogloss/iterations
    return (totalLogloss/iterations), loglosses
    
def innerLoopLogLoss(trainIndex, testIndex, X, Y, classifier):
    global totalLogloss
    global iterations
    
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = Y[trainIndex]
    testLabels = Y[testIndex]

    predictions, trips = classifier(trainSet, trainLabels, testSet)
    logloss = log_loss(testLabels, predictions, trips)	
    with lock:    
        print 'Log Loss: ', logloss
        loglosses.append(logloss)
        iterations += 1
    
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
    
def countActiveThreads(threads):
    activeThreads = 0
    for thread in threads:
        if (thread.isAlive()):
            activeThreads += 1
    return activeThreads
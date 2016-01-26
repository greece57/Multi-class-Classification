# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:54:53 2016

@author: Niko
"""

import numpy as np
import time
from helper import readFile, calcLogLoss
from classify import classifyRandomForest, classifySupportVectorMaschine, classifyDecisionTree
from classify import classifyGradientBoosting, classifyBayes, classifyLogistic
from createData import create

def classifyDataFile(file, classifierName = '', classifierOption = '', option = 'readFile'):
    if (option == 'readFile'):
        print 'Start reading'
        data = readFile(file,94248)
        data = np.delete(data, 0 , 1)
        print 'Stop reading'
    else:
        print 'Start creating Data'
        data = create(file, False)
        data = np.delete(data, 0, 0)
        print 'Finished creating Data'
        
    Labels = data[:,0]
    Set = np.delete(data, 0 , 1)
    
    data = []
    
    print 'Starting calculation: ' + time.ctime()
    
    if (classifierName == 'randomForest'):
        classifier = classifyRandomForest
    if (classifierName == 'SVM'):
        classifier = classifySupportVectorMaschine
    if (classifierName == 'GradientBoosting'):
        classifier = classifyGradientBoosting
    if (classifierName == 'Naive'):
        classifier = classifyBayes
    if (classifierName == 'Logistic'):
        classifier = classifyLogistic
    if (classifierName == 'Tree'):
        classifier = classifyDecisionTree
    
    totalLogLoss, loglosses = calcLogLoss(Set, Labels, classifier)
    
    print 'Finished calculation: ' + time.ctime()
    
    
    print 'Writing result to file'
    
    outputString = ""
    outputString += file + ", " + option + ", "
    outputString += classifierName + " " + "Option1: " + classifierOption + "\n"
    for logloss in loglosses:
        outputString += "LogLoss: "
        outputString += str(logloss)
        outputString += "\n"
    outputString += "Average LogLoss: " + str(totalLogLoss)
    
    outputString += "\n------------------\n"
        
    fw = open("result", 'a')
    fw.write(outputString)
    fw.close()
    
    print 'Finished calc LogLoss -> created result file'
    

if __name__ == "__main__":
    #classifyDataFile("train_sample_walmart_final_1000.csv",'randomForest', '10')
    #classifyDataFile("newData.csv",'randomForest', '10')
    classifyDataFile("train_small.csv",'randomForest', '100','calcFromFile')
    #classifyDataFile("train.csv",'randomForest', '10','calcFromFile')
    #classifyDataFile("walmart_train.csv",'randomForest','100')
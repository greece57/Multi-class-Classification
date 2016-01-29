# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:54:53 2016

@author: Niko
"""

import numpy as np
import time
from helper import readFile, createResultFile, chooseClassifier
from log_loss import calcLogLoss
from createData import create

def classifyDataFile(fileConfig, classifierName):
    """Classifies a given .csv-Document with a given classifier
    Calculates a 10 KFold Logloss and prints it into a 'result' file
    
    Parameters
    -----------
    :param fileConfig: touple with 
    [0]: FileName 
    [1]: NumberOfLines of File 
    [2]: 
        'readFile' for readingFile
        'createFile' for create new Data out of File
    :param classifierName:  name of the classifier
                            {randomForest, SVM, GradientBoosting, 
                             Naive, Logistic, Tree}
    """
    
    # ReadFile or CalcFile for classification
    if (fileConfig[2] == 'readFile'):
        print 'Start reading'
        data = readFile(fileConfig[0], fileConfig[1])
        print 'Stop reading'
    else:
        print 'Start creating Data'
        data = create(fileConfig)
        data = np.delete(data, 0, 0)
        print 'Finished creating Data'
        
    # Seperate Labels and the Rest of the dataSet
    Labels = data[:,0]
    Set = np.delete(data, 0 , 1)
    
    # Release dataArray for memory saving
    data = []
    
    # Choose Classifier according to given ClassifierName
    classifier = chooseClassifier(classifierName)
    
    startTime = time.ctime()
    print 'Starting calculation: ' + startTime
    
    # Calc the indipendent LogLosses and the Average Final LogLoss
    averageLogLoss, loglosses = calcLogLoss(Set, Labels, classifier)
    
    endTime = time.ctime()
    print 'Finished calculation: ' + endTime
    
    
    print 'Writing result to file'
    createResultFile(fileConfig, classifierName, 
                     averageLogLoss, loglosses,
                     startTime, endTime)
    
    
    print 'Finished calc LogLoss -> extended result file'
    

if __name__ == "__main__":
    # Full File
    fileConfig = ('train.csv', 647055, 'createFile')
    # touple beeing (FileName, NumberOfLines in File, readFile || createFile)
    
    # Small File
    #fileConfig = ('train_small.csv', 5000, 'createFile')
    
    # Run Create Data first before running this
    #fileConfig = ('newData.csv', 852, 'readFile')
    
    classifierName = 'randomForest'
    classifyDataFile(fileConfig, classifierName)

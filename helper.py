# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np
import csv as csv
from classify import classifyRandomForest, classifySupportVectorMaschine
from classify import classifyDecisionTree, classifyGradientBoosting
from classify import classifyBayes, classifyLogistic

   
def readFile(fileName, maxRows = -1, convertToInt = True):
    # Load data

    csv_file = open(fileName, 'r', encoding="utf8")
    csv_file_object = csv.reader(csv_file) # Load in the csv file
    next(csv_file_object) # Skip the fist line as it is a header
    rows=[] # Create a variable to hold the data


    cRow = 1
    nextLimit = 5
    for row in csv_file_object: # Skip through each row in the csv file,
        rows.append(row[0:]) 	# adding each row to the data variable
        
        if (maxRows > 0):
            cRow = cRow + 1
            percent = (100*cRow/maxRows)
            if (percent == nextLimit):
                nextLimit += 5
                print('Progress: ', percent)
                if (cRow == maxRows):
                    break
    
    if convertToInt:
        data = np.array(rows).astype('float32') 		# Then convert from a list to an array
    else:
        data = np.array(rows)
        
    print('Bytes: ', data.nbytes)
    
    rows = []
    
    return data
    
    
def createNumberedDictionary(data, normalize=False):
    """ create a Dictionary out of array
    Example:
    data = ['a','b','c']
    return = {'a': 0, 'b': 1, 'c': 2}
    """
    data = np.unique(data)    
    if normalize:    
        step = 1/(len(data)-1)
    else:
        step = 1
    entryNr = 0
    dataDirectory = dict()
    for i in range(data.shape[0]):
        dataDirectory[data[i]] = entryNr
        entryNr += step
    return dataDirectory  
    
    
def chooseClassifier(classifierName):
    # returns classifier Method according to Name
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
        
    return classifier


def createResultFile(fileConfig, classifierName, averageLogLoss, 
                     loglosses, startTime, endTime):
    # append LogLosses and AverageLogLoss to result-file
    outputString = ""
    outputString += fileConfig[0] + ", " + fileConfig[2] + ", "
    outputString += classifierName + " " + "\n"
    outputString += "StartTime: " + startTime + "\n"
    outputString += "EndTime: " + endTime + "\n \n"
    for logloss in loglosses:
        outputString += "LogLoss: "
        outputString += str(logloss)
        outputString += "\n"
    outputString += "Average LogLoss: " + str(averageLogLoss)
    
    outputString += "\n------------------\n"
        
    fw = open("result", 'a')
    fw.write(outputString)
    fw.close()
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np
import csv as csv
from log_loss import log_loss
from sklearn.cross_validation import KFold

def createNumberedDictionary(data, normalize=False):
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
    
    
def readFileInclHeader(name, maxRows = -1):
    # Load data
    csv_file_object = csv.reader(open(name, 'rb')) # Load in the csv file
    header = csv_file_object.next() 					  # Skip the fist line as it is a header
    rows=[] 											  # Create a variable to hold the data

    cRow = 1.0
    for row in csv_file_object: # Skip through each row in the csv file,
        rows.append(row[0:]) 	# adding each row to the data variable
        
        if (maxRows > 0):
            cRow = cRow + 1.0
            percent = (cRow/maxRows)*100.0
            if (percent % 1 == 0):
                print 'Progress: ', percent
            
    data = np.array(rows) 		# Then convert from a list to an array
    
    return data, header
    
def readFile(name, maxRows = -1):
    data, header = readFileInclHeader(name, maxRows)
    return data
    
def calcLogLoss(X,Y,classifier):
    kf = KFold(X.shape[0], n_folds=10) # Initialize cross validation

    iterations = 0 # Variable that will store the total iterations  
    totalLogloss = 0 # Variable that will store the correctly predicted intances  

    for trainIndex, testIndex in kf:
        trainSet = X[trainIndex]
        testSet = X[testIndex]
        trainLabels = Y[trainIndex]
        testLabels = Y[testIndex]

        predictions, trips = classifier(trainSet, trainLabels, testSet)
        logloss = log_loss(testLabels, predictions, trips)	
        print 'Log Loss: ', logloss
        totalLogloss += logloss
        iterations += 1
    print 'Average Log Loss: ', totalLogloss/iterations
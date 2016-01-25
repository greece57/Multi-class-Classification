# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np
import csv as csv
from log_loss import calc

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
    
    
def readFileInclHeader(name, maxRows = -1, convertToInt = True):
    # Load data
    csv_file_object = csv.reader(open(name, 'rb')) # Load in the csv file
    header = csv_file_object.next() 					  # Skip the fist line as it is a header
    rows=[] 											  # Create a variable to hold the data


    cRow = 1
    nextLimit = 5
    for row in csv_file_object: # Skip through each row in the csv file,
        rows.append(row[0:]) 	# adding each row to the data variable
        
        if (maxRows > 0):
            cRow = cRow + 1
            percent = (100*cRow/maxRows)
            if (percent == nextLimit):
                nextLimit += 5
                print 'Progress: ', percent
                if (cRow == maxRows):
                    break
    
    if convertToInt:
        data = np.array(rows).astype('int8') 		# Then convert from a list to an array
    else:
        data = np.array(rows)
        
    print 'Bytes: ', data.nbytes    
    
    rows = []
    return data, header
    
def readFile(name, maxRows = -1, convertToInt = True):
    data, header = readFileInclHeader(name, maxRows, convertToInt)
    #data = np.genfromtxt(name, np.int8, delimiter=',', names=True) 
    return data
    
def calcLogLoss(X,Y,classifier):
    return calc(X,Y,classifier)
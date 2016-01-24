# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np
import csv as csv
import threading
from log_loss import log_loss, calc

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
                if (cRow == maxRows):
                    break
            
    data = np.array(rows) 		# Then convert from a list to an array
    
    return data, header
    
def readFile(name, maxRows = -1):
    data, header = readFileInclHeader(name, maxRows)
    return data
    
def calcLogLoss(X,Y,classifier):
    calc(X,Y,classifier)
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:54:53 2016

@author: Niko
"""

import numpy as np
from helper import readFile, calcLogLoss
from classify import classifyRandomForest
from createData import create

def classifyDataFile(file, option = 'readData'):
    if (option == 'readData'):
        print 'Start reading'
        data = readFile(file,1000)
        print 'Stop reading'
    else:
        print 'Start creating Data'
        data = create(file, False)
        data = np.delete(data, 0, 0)
        print 'Finished creating Data'
        
    Labels = data[:,0]
    Set = np.delete(data, 0 , 1)
    
    data = []
    
    print 'Starting calculation'
    
    totalLogLoss, loglosses = calcLogLoss(Set, Labels, classifyRandomForest, 4)
    
    print 'Writing result to file'
    
    outputString = ""
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
    #classifyDataFile("train_sample_walmart_final_1000.csv")
    #classifyDataFile("newData.csv")
    classifyDataFile("train_small.csv",'calcFromFile')
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:54:53 2016

@author: Niko
"""

import numpy as np
from helper import readFile, calcLogLoss
from classify import classifyRandomForest

print 'Start reading'
data = readFile("train_walmart_final.csv",94247)
print 'Stop reading'

Labels = data[:,0]
Set = np.delete(data, 0 , 1)

print 'Starting calculation'

calcLogLoss(Set, Labels, classifyRandomForest)


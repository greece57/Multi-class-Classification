# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np

def createNumberedDictionary(data):
    data = np.unique(data)    
    entryNr = 0
    dataDirectory = dict()
    for i in range(data.shape[0]):
        dataDirectory[data[i]] = entryNr
        entryNr += 1
    return dataDirectory    
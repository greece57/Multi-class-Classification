# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:01:56 2016

@author: Niko
"""

import numpy as np

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
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:38:51 2016

@author: Niko
"""

import matplotlib.pyplot as plt
import numpy as np
from helper import readFile

data = readFile('train.csv')

dataFiltered = data[data[:,6]=='1017',:]

#AllTripTypes = data[:,0].astype(int)
AllTripTypes = dataFiltered[:,0].astype(int)
UniqueTripTypes = np.unique(data[:,0]).astype(int)
NumberOfTripTypes = len(UniqueTripTypes) - 1
AllTripTypes[AllTripTypes > 900] = 0

plt.hist(AllTripTypes, np.amax(UniqueTripTypes)+ 1)
plt.show()
    
#plot(TripTypes, Occurences)

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:38:51 2016

@author: Niko
"""

import matplotlib.pyplot as plt
import numpy as np
from helper import readFile
from helper import createNumberedDictionary

def plotHistogram(data, column = -1, value = 0):
    dataFiltered = data[data[:,column]==value,:]

    if (row == -1):
        AllTripTypes = data[:,0].astype(int)
    else:
        AllTripTypes = dataFiltered[:,0].astype(int)
    UniqueTripTypes = np.unique(data[:,0]).astype(int)
    NumberOfTripTypes = len(UniqueTripTypes) - 1
    AllTripTypes[AllTripTypes > 900] = 0
    
    plt.hist(AllTripTypes, np.amax(UniqueTripTypes)+ 1)
    plt.show()
    
    #plot(TripTypes, Occurences)
    
def plotCategories(data, columnFeatureX, columnFeatureY):
    data[data[:,0] > 900, 0] = 0
    dataFiltered = data[:,(0,columnFeatureX,columnFeatureY)]
    
    dictTripTypes = createNumberedDictionary(dataFiltered[:,0])
    dictTripTypes = dict((y,x) for x,y in dictTripTypes.iteritems())

    featureXDict = createNumberedDictionary(dataFiltered[:,1])
    featureYDict = createNumberedDictionary(dataFiltered[:,2])    
    
    NumberOfTripTypes = len(np.unique(data[:,0])) - 1
    listTripTypes = []
    
    for i in range(0, NumberOfTripTypes):
        tripType = dictTripTypes[i]
        dataTripType = dataFiltered[dataFiltered[:,0] == tripType]
        dataTripType = dataTripType[:,(1,2)]
        for j in range(0, len(dataTripType)):
            dataTripType[j,0] = featureXDict[dataTripType[j,0]]
            dataTripType[j,1] = featureYDict[dataTripType[j,1]]
        listTripTypes.append(dataTripType)
    
    for tripType in listTripTypes:
        plt.plot(tripType[:,0], tripType[:,1], 'o')
    plt.show()
    
    


if __name__ == "__main__":
    data = readFile('train_small.csv')

    plotCategories(data,5,4)
    #plotHistogram(data)
    #plotHistogram(data, 6, '1017')

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:14:22 2016

@author: Niko
"""

import numpy as np
from helper import readFileInclHeader, createNumberedDictionary

class Visit:
    
    def __init__(self, tripType, visitNumber, weekday):
        self.tripType = tripType
        self.visitNumber = visitNumber
        self.weekday = weekday
        self.upc = []
        self.scanCounts = []
        self.departments = []
        self.fineLines = []

def createData(filename, exportToFile = True):
    data, header = readFileInclHeader(filename, 647054, False)
    
    visits = []
    
    print 'Start reading entries'
    currentVisit = Visit(-1,-1,-1)
    for entry in data:
        if (entry[5]!='NULL'):
            if (entry[1] != currentVisit.visitNumber):
                v = Visit(entry[0],entry[1],entry[2])
                currentVisit = v
                visits.append(currentVisit)
            currentVisit.upc.append(entry[3])
            currentVisit.scanCounts.append(entry[4])
            currentVisit.departments.append(entry[5])
            currentVisit.fineLines.append(entry[6])
    
    print 'Creating data for new Matrix'
    noVisits = len(visits)
    departmentsDict = createNumberedDictionary(data[:,5])
    fineLineDict = createNumberedDictionary(data[:,6])
    weekdayDict = createNumberedDictionary(data[:,2])
    departments = np.unique(data[:,5])
    noDepartments = len(departments)
    fineLines = np.unique(data[:,6])
    noFineLines = len(fineLines)
    noFeatures = 3 + noDepartments + noFineLines
    
    newData = np.zeros((noVisits + 1, noFeatures))
    newData = newData[:].astype('int8')
    
    print 'Filling new Matrix'
    
    for i in range(0,len(visits)):
        row = i + 1
        newData[row,0] = visits[i].tripType
        newData[row,1] = weekdayDict[visits[i].weekday]
        totalScanCount = 0
        for j in range(0,len(visits[i].scanCounts)):
            dep = visits[i].departments[j]
            fL = visits[i].fineLines[j]
            sC = visits[i].scanCounts[j].astype('int8')
            depColumn = departmentsDict[dep] + 3
            fLColumn = fineLineDict[fL] + noDepartments + 3
            
            totalScanCount = totalScanCount + sC
            newData[row,depColumn] = newData[row,depColumn] + sC
            newData[row,fLColumn] = newData[row,fLColumn] + sC
        newData[row,3] = totalScanCount
    
    #newData = newData[:].astype('str')
    
    #newData[0,0] = "TripType"
    #newData[0,1] = "Weekday"
    #newData[0,2] = "ScanCount"
    #for i in range(0,noDepartments):
    #    newData[0,i+3] = departments[i]
    #for i in range(0,noFineLines):
    #    newData[0,i+noDepartments+3] = fineLines[i]

    if exportToFile:
        print 'Exporting new Matrix'
        np.savetxt("newData.csv", newData, delimiter=",", fmt="%s")
        
    return newData


# MAIN
createData("train_small.csv")
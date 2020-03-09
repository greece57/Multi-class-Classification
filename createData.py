# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:14:22 2016

@author: Niko
"""

import numpy as np
from helper import readFile, createNumberedDictionary

class Visit:
    # Class for one Visit with different bought products
    def __init__(self, tripType, visitNumber, weekday):
        self.tripType = tripType
        self.visitNumber = visitNumber
        self.weekday = weekday
        self.upc = []
        self.scanCounts = []
        self.departments = []
        self.fineLines = []

def create(fileConfig, exportToFile = ""):
    """Reads train.csv-files with original walmart Data 
    and creates a new FeatureSet with Departments and FineLines as Attributes
    containing the number of items bought from the Department/FineLine as Value
    
    New Data Matrix Column Names:
    | TripType | Weekday [0-6] | TotalScanCount | _
    _ | Department 1 | ... | Department X | _
    _ | FineLine# 1 | ... | FineLine# X |
    
    When Exported into a File Column Names are not saved as String.
    However there will be a header line created containing zeros as values.
    
    
    Parameters
    -----------
    :param fileConfig: touple with 
    [0]: FileName 
    [1]: NumberOfLines of File 
    
    :param exportToFile: Specify new fileName if new Matrix shall be exported
                         Leave Empty if Matrix shall not be saved to a file
                         
    :return : new dataMatrix
    """
    data = readFile(fileConfig[0], fileConfig[1], False)
    
    visits = []
    
    # create Array of unique Visits
    print('Start reading entries')
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
    
    print('Creating data for new Matrix')
    # create Dictionaries to fill newData-Matrix
    noVisits = len(visits)
    departmentsDict = createNumberedDictionary(data[:,5])
    fineLineDict = createNumberedDictionary(data[:,6])
    weekdayDict = createNumberedDictionary(data[:,2])
    departments = np.unique(data[:,5])
    noDepartments = len(departments)
    fineLines = np.unique(data[:,6])
    noFineLines = len(fineLines)
    
    # create new empty Data array
    noFeatures = 3 + noDepartments + noFineLines    
    newData = np.zeros((noVisits + 1, noFeatures))
    newData = newData[:].astype('int8')
    
    print('Filling new Matrix')
    for i in range(0,len(visits)):
        # for each visit write TripType and Weekday
        row = i + 1
        newData[row,0] = visits[i].tripType
        newData[row,1] = weekdayDict[visits[i].weekday]
        totalScanCount = 0
        
        for j in range(0,len(visits[i].scanCounts)):
            # for each Row in original Matrix fill new Matrix             
            # by writing scanCount of specific Deparmtent and FineLine
            # in the specific FeatureRow
            dep = visits[i].departments[j]
            fL = visits[i].fineLines[j]
            sC = visits[i].scanCounts[j].astype('int8')
            depColumn = departmentsDict[dep] + 3
            fLColumn = fineLineDict[fL] + noDepartments + 3
            
            totalScanCount = totalScanCount + sC # increase totalScanCount
            newData[row,depColumn] = newData[row,depColumn] + sC
            newData[row,fLColumn] = newData[row,fLColumn] + sC
        
        # write totalScanCount as Feature
        newData[row,3] = totalScanCount

    if exportToFile != '':
        # if there is a fileName specified write newMatrix into this file
        print('Exporting new Matrix')
        np.savetxt(exportToFile, newData, delimiter=",", fmt="%s")
        
    return newData


# MAIN
if __name__ == "__main__":
    fileConfig = ('train_small.csv', 5000)
    # touple beeing (FileName, NumberOfLines in File)
    create(fileConfig, "newData.csv")
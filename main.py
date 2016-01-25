import numpy as np
from classify import classify
from classify import classifyBayes
from classify import classifyRandomForest
from helper import createNumberedDictionary, readFile, calcLogLoss

data = readFile('train_small.csv', convertToInt=False)

daysIndex = createNumberedDictionary(data[:,2]) # A dictionary keyed by day to its index
departmentIndex = createNumberedDictionary(data[:,5])

numVisits = len(np.unique(data[:,1])) # Number of distinct visits

X = np.zeros((numVisits, len(departmentIndex))) # Matrix containing the day and department of each visit
Y = np.zeros(numVisits) # A matrix containing the trip types of the visits

previousVisit = 0
index = -1
for i in range(data.shape[0]):
    if data[i,1] != previousVisit: 		# If visit number has changed, initialize a new visit
        index += 1						# The index of the new visit
        num_products = 1				# Set the number of products to 1
        previousVisit = data[i,1]			# Set previous visit number to the current visit
        weekday = daysIndex[data[i,2]]
        department = departmentIndex[data[i,5]]
        #X[index,weekday] = 1        
        #X[index,0] = weekday # Set the day of the visit
        X[index,department] = 1 # Set the department
        Y[index] = int(data[i,0])			# Store the type of the trip of the current visit
    else: 								# If visit number has not changed, it's still the same visit
        num_products += 1				# Increase the number of products of the current visit
        #department = departmentIndex[data[i,5]]
        #X[index,department] = 1
        #Y[index] = int(data[i,0])
	

calcLogLoss(X,Y,classify)

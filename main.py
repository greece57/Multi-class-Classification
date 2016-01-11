import numpy as np
from log_loss import log_loss
from sklearn.cross_validation import KFold
#from classify import classify
from classify import classifyBayes
from helper import createNumberedDictionary, readFile

data = readFile('train_small.csv')

daysIndex = createNumberedDictionary(data[:,2]) # A dictionary keyed by day to its index
departmentIndex = createNumberedDictionary(data[:,5])

numVisits = len(np.unique(data[:,1])) # Number of distinct visits

X = np.zeros((numVisits, len(daysIndex))) # Matrix containing the day and department of each visit
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
        X[index,0] = weekday # Set the day of the visit
        X[index,1] = department # Set the department
        Y[index] = int(data[i,0])			# Store the type of the trip of the current visit
    else: 								# If visit number has not changed, it's still the same visit
        num_products += 1				# Increase the number of products of the current visit
	

kf = KFold(X.shape[0], n_folds=10) # Initialize cross validation

iterations = 0 # Variable that will store the total iterations  
totalLogloss = 0 # Variable that will store the correctly predicted intances  

for trainIndex, testIndex in kf:
	trainSet = X[trainIndex]
	testSet = X[testIndex]
	trainLabels = Y[trainIndex]
	testLabels = Y[testIndex]

	predictions, trips = classifyBayes(trainSet, trainLabels, testSet)
	logloss = log_loss(testLabels, predictions, trips)	
	print 'Log Loss: ', logloss
	totalLogloss += logloss
	iterations += 1
print 'Average Log Loss: ', totalLogloss/iterations

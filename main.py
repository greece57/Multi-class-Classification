import numpy as np
import csv as csv
from log_loss import log_loss
from sklearn.cross_validation import KFold
from classify import classifyLogisticRegression, classifyRandomForest

# Load data
csv_file_object = csv.reader(open('walmart_train.csv', 'rb')) # Load in the csv file
header = csv_file_object.next() 					  # Skip the fist line as it is a header
rows=[] 											  # Create a variable to hold the data

for row in csv_file_object: # Skip through each row in the csv file,
    rows.append(row[0:]) 	# adding each row to the data variable
data = np.array(rows).astype('int') 		# Then convert from a list to an array

#data = data[range(1000),:] # take only first 500 rows of dataset

Y = data[:,0]
X = np.delete(data, 0, 1)

kf = KFold(X.shape[0], n_folds=10) # Initialize cross validation

iterations = 0 # Variable that will store the total iterations  
totalLogloss = 0 # Variable that will store the correctly predicted intances  

for trainIndex, testIndex in kf:
	trainSet = X[trainIndex]
	testSet = X[testIndex]
	trainLabels = Y[trainIndex]
	testLabels = Y[testIndex]

	predictions, trips = classifyLogisticRegression(trainSet, trainLabels, testSet)
	logloss = log_loss(testLabels, predictions, trips)	
	print 'Log Loss: ', logloss
	totalLogloss += logloss
	iterations += 1
print 'Average Log Loss Logistic Regression: ', totalLogloss/iterations

iterations = 0 # Variable that will store the total iterations  
totalLogloss = 0 # Variable that will store the correctly predicted intances 

for trainIndex, testIndex in kf:
	trainSet = X[trainIndex]
	testSet = X[testIndex]
	trainLabels = Y[trainIndex]
	testLabels = Y[testIndex]

	predictions, trips = classifyRandomForest(trainSet, trainLabels, testSet)
	logloss = log_loss(testLabels, predictions, trips)	
	print 'Log Loss: ', logloss
	totalLogloss += logloss
	iterations += 1
print 'Average Log Loss Random Forest: ', totalLogloss/iterations

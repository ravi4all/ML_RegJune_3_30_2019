import math
import csv
import random

def loadDataset(filename):
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def str_to_float(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])

def minMaxValues():
    minMax = []
    for i in range(len(x[0])):
#    	col = []
#    	for j in range(len(x)):
#    		col.append(x[j][i])
        col = [row[i] for row in dataset]
    	minVal = min(col)
    	maxVal = max(col)
    	minMax.append([minVal, maxVal])
    return minMax

def normalization():
#    x - min(x)/max(x) - min(x)
    pass

def crossValidation():
    pass

def predict(row,coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score():
    pass

def evaluateAlgorithm():
    pass

def sgd():
    pass

def logisticRegression():
    pass

filename = 'data.csv'
dataset = loadDataset(filename)
str_to_float(dataset)












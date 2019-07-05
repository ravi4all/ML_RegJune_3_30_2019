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

def minMaxValues(dataset):
    minMax = []
    for i in range(len(dataset[0])):
        col = [row[i] for row in dataset]
        minVal = min(col)
        maxVal = max(col)
        minMax.append([minVal, maxVal])
    return minMax

def normalization():
    
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            numer = dataset[i][j] - minMax[j][0]
            denom = minMax[j][1] - minMax[j][0]
            dataset[i][j] = numer / denom

def crossValidation(dataset, k=5):
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / k)
    folds = []
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def predict(row,coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score(pred,actual):
    count = 0
    for i in range(len(pred)):
        if actual[i] == pred[i]:
            count += 1
    return count / len(pred) * 100

def evaluateAlgorithm(dataset, epochs, alpha):
    scores = []
    folds = crossValidation(dataset)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train, [])
        test = []
        for row in fold:
            rowcopy = list(row)
            rowcopy[-1] = None
            test.append(rowcopy)
        pred = logisticRegression(train, test, epochs, alpha)
        actual = [row[-1] for row in fold]
        score = accuracy_score(pred,actual)
        scores.append(score)
    return scores

def sgd(dataset,epochs,alpha):
    coef = [0] * len(dataset[0])
    for epoch in range(epochs):
        for row in dataset:
            pred = predict(row, coef)
            loss = pred - row[-1]
            coef[0] = coef[0] - alpha * loss
            for j in range(len(row) - 1):
                coef[j+1] = coef[j+1] - alpha * loss * row[j]
    return coef

def logisticRegression(train,test,epochs,alpha):
    coef = sgd(train,epochs,alpha)
    predictions = []
    for row in test:
        pred = predict(row,coef)
        predictions.append(round(pred))
    return predictions

filename = 'data.csv'
dataset = loadDataset(filename)
str_to_float(dataset)
minMax = minMaxValues(dataset)
normalization()
epochs = 5000
alpha = 0.01
acc_scores = evaluateAlgorithm(dataset,epochs, alpha)
print(acc_scores)

avgScore = sum(acc_scores) / len(acc_scores)
print(avgScore)





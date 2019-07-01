Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x = np.array([5,6,7,4,8,2,3,1,7,9])
>>> len(x)
10
>>> labels = np.array([0,0,0,0,0,1,1,1,1,1])
>>> np.argsort(x)
array([7, 5, 6, 3, 0, 1, 2, 8, 4, 9], dtype=int64)
>>> lab = np.argsort(x)
>>> labels[lab]
array([1, 1, 1, 0, 0, 0, 0, 1, 0, 1])
>>> 
>>> labels[lab][:5]
array([1, 1, 1, 0, 0])
>>> sortedLabels = labels[lab][:5]
>>> count = np.unique(sortedLabels, return_counts=True)
>>> count
(array([0, 1]), array([2, 3], dtype=int64))
>>> count[0]
array([0, 1])
>>> count[0][np.argmax(count[1])]
1
>>> 

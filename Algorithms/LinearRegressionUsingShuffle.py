#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score,ShuffleSplit
from sklearn import preprocessing
from sklearn import datasets
from sklearn.utils import shuffle
import numpy as np

boston = datasets.load_boston()
X, Y = shuffle(boston.data, boston.target, random_state=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)


regressor = LinearRegression()
shuffle = ShuffleSplit(n_splits=10,test_size=0.3)

scores = cross_val_score(regressor,X,Y,cv=shuffle)
print("Shuffle : ")
for score in scores:
	print(score)
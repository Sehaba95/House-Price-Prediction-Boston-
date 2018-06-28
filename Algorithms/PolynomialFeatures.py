#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn import datasets
from sklearn.utils import shuffle
import numpy as np

boston = datasets.load_boston()
X, y = shuffle(boston.data, boston.target, random_state=13)
X = X.astype(np.float32)
poly = preprocessing.PolynomialFeatures(degree=2)
X =  poly.fit_transform(X)
offset = int(X.shape[0] * 0.9)
X_train, Y_train = X[:offset], y[:offset]
X_test, Y_test = X[offset:], y[offset:]



regressor = LinearRegression()
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)
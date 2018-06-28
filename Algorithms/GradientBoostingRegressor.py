#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor
from sklearn import datasets
from sklearn.utils import shuffle
import numpy as np

boston = datasets.load_boston()
X, Y = shuffle(boston.data, boston.target, random_state=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, Y_train = X[:offset], Y[:offset]
X_test, Y_test = X[offset:], Y[offset:]

regressor = GradientBoostingRegressor(n_estimators=120, learning_rate=0.2,max_depth=2, random_state=0, loss='ls')
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)
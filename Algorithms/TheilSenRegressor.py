#!/usr/bin/env python 

import pandas as pd
from sklearn.linear_model import TheilSenRegressor
from sklearn import datasets
from sklearn.utils import shuffle
import numpy as np

boston = datasets.load_boston()
X, y = shuffle(boston.data, boston.target, random_state=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)
X_train, Y_train = X[:offset], y[:offset]
X_test, Y_test = X[offset:], y[offset:]


regressor = TheilSenRegressor(random_state=0)
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)
#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv('https://raw.githubusercontent.com/positivee27/stats418-Final-Project/master/scripts/Moviedata%201.csv', error_bad_lines=False)

y = data['votes']
train1 = data.iloc[:,1:3]

col_imp = ["imdb", "metascore	"]

regr = LinearRegression()
regr.fit(train1, y)

def predict(dict_values, col_imp=col_imp, regr=regr):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = regr.predict(x)[0]
    return y_pred
#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv("https://raw.githubusercontent.com/positivee27/stats418-Mtcars-Flask-Api/master/scripts/mtcars.csv")

y = data['mpg']
train1 = data.iloc[:,3:8]

col_imp = ["disp", "hp", "dart", "wt", "qsec"]

regr = LinearRegression()
regr.fit(train1, y)

def predict(dict_values, col_imp=col_imp, regr=regr):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = regr.predict(x)[0]
    return y_pred
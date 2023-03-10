# -*- coding: utf-8 -*-
"""Logistic regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GiaWmWCbsA_zi_e6YI1XMt_s5eWfIIxn
"""

import pandas as pd
import plotly.express as px 
df=pd.read_csv("https://raw.githubusercontent.com/mamtawardhani/Datasets-for-linear-and-logistic-regression/main/score-accepted.csv")
print(df)

score_list=df["Score"].tolist()
accepted_list=df["Accepted"].tolist()
print(score_list)
print(accepted_list)

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.reshape(score_list,(len(score_list),1))
Y=np.reshape(accepted_list,(len(accepted_list),1))
lr=LogisticRegression()
lr.fit(X,Y)
def model(x):
  return 1/(1+np.exp(-x))
chances=model(X*lr.coef_+lr.intercept_).ravel()
#numpy is a python library for numerical computing.It provides a powerful array data structure and a set of functions for performing mathematical operations on these arrays effeiciently.
#np.reshape() is used to change the shape(dimensions) of an array without changing its data.
#ravel is used to flatten a multi-dimensional array into one dimensional array.ravel() returns a flattened array that contains all the elements of input array in a single row,in the same order as they appear in original array.

user_score=float(input("Enter your marks here:-"))
chances=model(user_score*lr.coef_+lr.intercept_).ravel()[0]
if chances <=0.01:
  print("The student will not get accepted")
elif chances >=1:
  print("The student will get accepted!")
elif chances <0.5:
  print("The student might not get accepted")
else:
  print("The student may get accepted")
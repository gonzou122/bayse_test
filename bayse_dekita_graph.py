# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J2GjM1pigwOh0zjNXwuXhQpJGSBh9n0y
"""

import pystan

!pip install arviz
import arviz

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.style.use('ggplot')

df = pd.read_csv('/content/data.csv')

df

plt.scatter(x=df['data'],y=df['parcent'])
plt.figure

x = df.iloc[:, 0]
y = df.iloc[:, 1]

x_pred = [i for i in range(13,51)]

x_pred = np.array(x_pred)

x_pred = pd.Series(x_pred)

y

print(f'{x.shape}')
print(f'{y.shape}')
print(f'{x_pred.shape}')

sm = pystan.StanModel(file = '/content/reg2.stan')

fit = sm.sampling(
    data = dict(
        N = n,
        x = x,
        y = y,
        N_pred = len(x_pred),
        x_pred = x_pred
        ),
    seed = 1234,
    iter = 5000,
    warmup = 1000,
    chains = 4)

arviz.plot_trace(fit)
print(fit)

temp = [i for i in range(0,51)]
temp

temp2 = []
for i in range(0,51):
  a = 68.86 + (-0.11 * temp[i])
  temp2.append(a)

temp2

plt.scatter(x=df['data'],y=df['parcent'])
plt.plot(temp,temp2)
plt.figure


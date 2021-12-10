import numpy as np
import pandas as pd

def find_err(x, y, b_exist=False):
    mxsq = np.mean(x ** 2)
    mysq = np.mean(y ** 2)
    xy = []
    for i in range(len(x)):
        xy.append(x[i] * y[i])
    
    xy = np.array(xy)
    mxy = np.mean(xy)

    if not b_exist:
        k = mxy / mxsq

    print(0.5 * np.sqrt(mysq / mxsq - k ** 2))

df = pd.read_csv('/Users/avarlamov/ML_learning/graphs/data145.csv')

t = np.array(df.loc[:, ['t']]).flatten()
u_sq = np.array([141, 169, 189, 211, 231]) ** 2

find_err(u_sq, t)
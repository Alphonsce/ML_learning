import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

df1 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/first.csv')
df2 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/second.csv')
df3 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/third.csv')

x1 = df1.x
p1 = df1.p

x2 = df2.x
p2 = df2.p

x3 = df3.x
p3 = df3.p

plt.scatter(x1, p1, label='первая трубка')
plt.scatter(x2, p2, label='вторая трубка')
plt.scatter(x3, p3, label='третья трубка')

plt.plot([0, 81.5, 131.5], [0, 68.6, 105.84])
plt.plot([0, 46.5], [0, 150.92])
plt.plot([0, 131.5], [0, 103.88])

plt.xlabel(r'$x$, см')
plt.ylabel(r'$P(x) - P(0)$, Па' )
plt.legend(loc='best', fontsize=14)
plt.grid('True')

plt.xticks(np.arange(0, 132, 5))

plt.show()
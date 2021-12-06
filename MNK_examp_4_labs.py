import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

df = pd.read_csv('/Users/avarlamov/starting_ML/data145.csv')

n = np.arange(1, 10)

first = np.array(df.loc[[0], 'n1':'n9']).flatten()
second = np.array(df.loc[[1], 'n1':'n9']).flatten()
third = np.array(df.loc[[2], 'n1':'n9']).flatten()
fourth = np.array(df.loc[[3], 'n1':'n9']).flatten()
fifth = np.array(df.loc[[4], 'n1':'n9']).flatten()

a1 = np.polyfit(n, first, deg=1, cov=True)      #   возвращает array([коэффициенты МНК]), array([[a, b],[c, d]]) - диагональные элементы - погрешности
a2 = np.polyfit(n, second, deg=1, cov=True)
a3 = np.polyfit(n, third, deg=1, cov=True)
a4 = np.polyfit(n, fourth, deg=1, cov=True)
a5 = np.polyfit(n, fifth, deg=1, cov=True)

print(a1[0][0], a1[1])
print(a2[0][0], a2[1])
print(a3[0][0], a3[1])
print(a4[0][0], a4[1])
print(a5[0][0], a5[1])

plt.scatter(n ,first, label='$T_1$')
plt.scatter(n ,second, label='$T_2$')
plt.scatter(n ,third, label='$T_3$')
plt.scatter(n ,fourth, label='$T_4$')
plt.scatter(n ,fifth, label='$T_5$')

plt.plot(n, a1[0][0] * n)
plt.plot(n, a2[0][0] * n)
plt.plot(n, a3[0][0] * n)
plt.plot(n, a4[0][0] * n)
plt.plot(n, a5[0][0] * n)

plt.xlabel(r'$n$')
plt.ylabel(r'$ \nu_n $, Гц')
plt.xlim(xmin=0)
plt.ylim(0)
plt.legend()

plt.show()
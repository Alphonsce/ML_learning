import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/home/alphonse/Desktop/testdir/data132.csv')

P = df.iloc[:, 0]

y1 = df.iloc[:, 1]
y2 = df.iloc[:, 2]
y3 = df.iloc[:, 3]

k1 = 1
k2 = 1
k3 = 1

plt.scatter(y1, P, label='Эксп. точки стержень 1', color='blue')
plt.scatter(y2, P, label='Эксп. точки стержень 2', color='green')
plt.scatter(y3, P, label='Эксп. точки стержень 3', color='red')

plt.errorbar(y1, P, xerr=y1 * 0.03, ls='none', color='blue')
plt.errorbar(y2, P, xerr=y1 * 0.03, ls='none', color='green')
plt.errorbar(y3, P, xerr=y1 * 0.03, ls='none', color='red')

plt.plot(y1, k1 * y1, label='Эксп. зависимость стержень 1', color='blue')
plt.plot(y2, k2 * y2, label='Эксп. зависимость стержень 2', color='green')
plt.plot(y3, k3 * y3, label='Эксп. зависимость стержень 3', color='red')

plt.ylabel('$P$, Н')
plt.xlabel('$y$, м')
plt.legend(loc='best', fontsize=10)

plt.show()
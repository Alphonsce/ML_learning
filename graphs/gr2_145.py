import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/avarlamov/ML_learning/graphs/data145.csv')

t = np.array(df.loc[:, ['t']]).flatten()
u_sq = np.array([141, 169, 189, 211, 231]) ** 2
u_sq_errors = np.array([0.014, 0.05, 0.03, 0.056, 0.06])

for i in range(len(u_sq_errors)):
    u_sq_errors[i] *= u_sq[i]
print(u_sq_errors)


a = np.polyfit(u_sq, t, deg=1, cov=True)
print(a[0][0] * 1_000_000)
k = a[0][0] * 1000


plt.scatter((u_sq / 1000), t, label='экспериментальные точки', color='blue')
plt.plot((u_sq / 1000), k * (u_sq / 1000), label=r'экспериментальная зависимость $T=ku^2$', color='blue')
plt.errorbar(u_sq / 1000, t, xerr=u_sq_errors / 1000, ls='none', color='blue')

plt.xlabel(r'$u^2 \cdot 10^{-3}$, $\frac{м^2}{с^2}$')
plt.ylabel(r'$ T $, Н')
plt.legend(loc='upper left', fontsize=10)

plt.show()
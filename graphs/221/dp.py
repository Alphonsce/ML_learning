import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log

def calculate_k(x, y, through_zero=False):
    '''Вычисление коэффициентов для аппроксимации зависимостью y = kx + b
    '''
    n = len(x)
    m_x = x.mean()
    m_y = y.mean()
    m_xx = (x * x). mean()
    m_yy = (y * y).mean()
    m_xy = (x * y).mean()
    m_x_m_x = x.mean() * x.mean()
    m_y_m_y = y.mean() * y.mean()

    k = 0
    s_k = 0
    b = 0
    s_b = 0

    if through_zero:
        k = m_xy / m_xx
        s_k = (1 / sqrt(n)) * sqrt((m_yy / m_xx) - k ** 2)
        return [k, s_k]

    else:
        k = (m_xy - m_x * m_y) / (m_xx - m_x_m_x)
        b = m_y - k * m_x

        s_k = (1 / sqrt(n)) * sqrt((m_yy - m_y_m_y) / (m_xx - m_x_m_x) - k ** 2)
        s_b = s_k * sqrt(m_xx - m_x_m_x)
        return [k, s_k, b, s_b]

df = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/dp.csv')

oneoverp = df['p'].map(lambda x: 1 / x)

plt.scatter(oneoverp, df.d, label='Экспериментальные точки', color ='blue')

xerr = []
yerr = []
for i in df.p:
    xerr.append(3 / i ** 2)
for i in df.d:
    yerr.append(0.01 * i)

plt.errorbar(oneoverp, df.d, xerr=xerr, yerr=yerr , ls='none', color='red')

k, s_k = calculate_k(oneoverp, df.d, True)[0], calculate_k(oneoverp, df.d, True)[1]
x = np.arange(0, 0.025, 0.001)
plt.plot(x, k * x, color='blue', label='Экстраполяция зависимости')

print(k, s_k)

plt.xlabel(r'$\dfrac{1}{P}, торр^{-1}$')
plt.ylabel(r'$D, \dfrac{см^2}{с}$')
plt.legend(loc='best')

plt.show()
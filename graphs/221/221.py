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

df1 = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/42torr.csv')
df2 = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/95torr.csv')
df3 = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/150torr.csv')
df4 = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/209torr.csv')
df5 = pd.read_csv('/Users/avarlamov/ML_learning/graphs/221/277torr.csv')

lnu1 = df1.u.map(lambda x: log(x))
lnu2 = df2.u.map(lambda x: log(x))
lnu3 = df3.u.map(lambda x: log(x))
lnu4 = df4.u.map(lambda x: log(x))
lnu5 = df5.u.map(lambda x: log(x))

k1, sk1, b1 = calculate_k(df1.t, lnu1)[0], calculate_k(df1.t, lnu1)[1], calculate_k(df1.t, lnu1)[2]
k2, sk2, b2 = calculate_k(df2.t, lnu2)[0], calculate_k(df2.t, lnu2)[1], calculate_k(df2.t, lnu2)[2]
k3, sk3, b3 = calculate_k(df3.t, lnu3)[0], calculate_k(df3.t, lnu3)[1], calculate_k(df3.t, lnu3)[2]
k4, sk4, b4 = calculate_k(df4.t, lnu4)[0], calculate_k(df4.t, lnu4)[1], calculate_k(df4.t, lnu4)[2]
k5, sk5, b5 = calculate_k(df5.t, lnu5)[0], calculate_k(df5.t, lnu5)[1], calculate_k(df5.t, lnu5)[2]

plt.plot(df1.t, k1 * df1.t + b1)
plt.plot(df2.t, k2 * df2.t + b2)
plt.plot(df3.t, k3 * df3.t + b3)
plt.plot(df4.t, k4 * df4.t + b4)
plt.plot(df5.t, k5 * df5.t + b5)

print(k1, sk1)
print(k2, sk2)
print(k3, sk3)
print(k4, sk4)
print(k5, sk5)

plt.xlabel(r'$t$, c', fontsize=14)
plt.ylabel(r'$\ln U$', fontsize=14)

plt.xticks(np.arange(0, 454, 30))

plt.show()
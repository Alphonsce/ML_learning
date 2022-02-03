import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

data2 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/qp3.csv')

print(data2)

def calculate_k(x, y, through_zero=False):
    '''
    Вычисление коэффициентов для аппроксимации зависимостью y = kx + b
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

# Ламинарные области для 3 трубки:
q1 = data2.loc[0:5, 'q']
p1 = data2.loc[0:5, 'p']

k1, s_k = calculate_k(p1, q1, True)[0], calculate_k(p1, q1, True)[1]

plt.scatter(data2.p, data2.q, label='Экспериментальные точки')
x = np.arange(0, 85)
plt.plot(x, k1 * x, label='Экспериментальная зависимость в области ламинарного режима')

#plt.axvline(x=161, linestyle='dashed', color='red', label='Переход к турбулентному режиму')

plt.xlabel(r'$\Delta P$, Па')
plt.ylabel(r'$Q, 10^{-5}\cdot \dfrac{кг}{c}$' )
plt.legend(loc='best')
plt.grid('True')
plt.xticks(np.arange(0, 500, 25))

plt.show()

print(k1, s_k)
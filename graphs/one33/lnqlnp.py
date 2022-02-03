import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, log

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

dfturb1 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/logplogq1.csv')

lnq1 = (dfturb1.copy().q).map(lambda x: log(x / 100000))
lnp1 = (dfturb1.p).map(lambda x: log(x / 1000))

print(calculate_k(lnp1, lnq1))

x = np.arange(-1.8, -0.6, 0.01)
plt.scatter(lnp1, lnq1)
plt.plot(x, calculate_k(lnp1, lnq1)[0] * x + calculate_k(lnp1, lnq1)[2], label='Первая трубка')

dfturb2 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/logplogq2.csv')

lnq2 = (dfturb2.copy().q).map(lambda x: log(x / 100000))
lnp2 = (dfturb2.p).map(lambda x: log(x / 1000))

print(calculate_k(lnp2, lnq2))

x = np.arange(-1.8, -0.6, 0.01)
plt.scatter(lnp2, lnq2)
plt.plot(x, calculate_k(lnp2, lnq2)[0] * x + calculate_k(lnp2, lnq2)[2], label='Вторая трубка')

dfturb3 = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/logplogq3.csv')

lnq3 = (dfturb3.copy().q).map(lambda x: log(x / 100000))
lnp3 = (dfturb3.p).map(lambda x: log(x / 1000))

print(calculate_k(lnp3, lnq3))

x = np.arange(-1.8, -0.6, 0.01)
plt.scatter(lnp3, lnq3)
plt.plot(x, calculate_k(lnp3, lnq3)[0] * x + calculate_k(lnp3, lnq3)[2], label='Третья трубка')


plt.xlabel(r'$\ln \Delta P$', fontsize=14)
plt.ylabel(r'$\ln Q$', fontsize=14)
plt.legend(loc='best', fontsize=14)

plt.show()
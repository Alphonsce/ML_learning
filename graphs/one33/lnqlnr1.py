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

dflam = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/loglam.csv')

lnq = (dflam.copy().q).map(lambda x: log(x / 100000))
lnr = (dflam.r).map(lambda x: log(x / 1000))

dfturb = pd.read_csv('/home/alphonse/ML_learning/graphs/one33/logturb.csv')

lnq1 = (dfturb.copy().q).map(lambda x: log(x / 100000))
lnr1 = (dfturb.r).map(lambda x: log(x / 1000))

print(calculate_k(lnr1, lnq1))
print(calculate_k(lnr, lnq))

x = np.arange(-6.5, -5)
plt.scatter(lnr, lnq)
plt.plot(x, calculate_k(lnr, lnq)[0] * x + calculate_k(lnr, lnq)[2], label='Ламинарный режим')
plt.scatter(lnr1, lnq1)
plt.plot(x, calculate_k(lnr1, lnq1)[0] * x + calculate_k(lnr1, lnq1)[2], label='Турбулентый режим')

plt.xlabel(r'$\ln r$', fontsize=14)
plt.ylabel(r'$\ln Q$', fontsize=14)
plt.legend(loc='best', fontsize=14)

plt.show()
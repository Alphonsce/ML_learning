import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import sqrt

def calculate_k(x, y, through_zero=False):
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

inc1 = pd.read_csv('increase1.csv')
inc2 = pd.read_csv('increase2.csv')
inc3 = pd.read_csv('increase3.csv')

dec1 = pd.read_csv('decrease1.csv')
dec2 = pd.read_csv('decrease2.csv')
dec3 = pd.read_csv('decrease3.csv')

arr_inc = [inc1, inc2, inc3]
arr_dec = [dec1, dec2, dec3]
for df in arr_inc:
    df = df[['t', 'lnp']]
    print(calculate_k(df.t, df.lnp))

for df in arr_dec:
    df = df[['t', 'p']]
    print(calculate_k(df.t, df.p))

print((0.146 + 0.142 + 0.147) / 3)
print((0.796 + 0.763 + 0.747) / 3)

plt.scatter(inc1.t, inc1.lnp)
plt.scatter(inc2.t, inc2.lnp)
plt.scatter(inc3.t, inc3.lnp)

plt.plot(np.arange(0, 18, 0.1), -0.320 * np.arange(0, 18, 0.1) -13.8)


# plt.scatter(dec1.t, dec1.p)
# plt.scatter(dec2.t, dec2.p)
# plt.scatter(dec3.t, dec3.p)

# plt.plot(np.arange(0, 83, 0.1), 0.768 * np.arange(0, 83, 0.1) + 9)

# plt.plot(np.arange(0, 83, 0.1), 0.768 * np.arange(0, 83, 0.1) + 9)

plt.xlabel(r'$t$, с')
plt.ylabel(r'$P, 10^{-5} торр$')

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from math import cos, sqrt, sin

ns = np.arange(1, 5000)
ans = np.array([])
summm = np.array([])

def transform(number):
    return sin(1 / (number ** 2))

for i in range(len(ns)):
    ans = np.append(ans, transform(ns[i]))

for i in range(len(ans)):
    current = sum(ans[:i])
    summm = np.append(summm, current)

plt.plot(ns, summm)

plt.show()
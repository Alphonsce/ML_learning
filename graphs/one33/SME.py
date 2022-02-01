import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]})

print(df.Apples.mean())

plt.plot(df.Apples, [1, 2])

plt.show()

def calculate_k(x, y, through_zero=False):
    if through_zero:
        pass
    
    else:
        pass
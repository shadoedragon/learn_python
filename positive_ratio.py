import numpy as np
import matplotlib.pyplot as mp

x = np.arange(1,100)
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([3.5, 7, 10.5, 14, 17.5])
y = x*x*x
mp.grid()
mp.plot(x, y, color='red')
mp.show()
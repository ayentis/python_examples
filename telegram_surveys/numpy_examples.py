import numpy as np
# a = np.linspace(1, 4, 4)
# b = a.reshape(2, 2)
# b[0, 0] = 0
# print(a[0] + b[0, 0] + b[1, 1])


a = np.arange(4)
print(a)
b = a.transpose()
print(b)
print( a.shape)
# x = a.shape == b.shape
# print(x)
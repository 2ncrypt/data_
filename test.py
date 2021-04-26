import numpy as np

np.random.seed(0)
a = np.random.rand(7)
print(a)

a = np.random.rand(7)
print(a)

c = np.random.rand(7)
print(c)
np.random.seed(3)
c = np.random.rand(7)
print(c)
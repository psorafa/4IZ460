import numpy as np

a = np.array([1,2,3,4]).reshape(2,2)
b = np.array([5,6,7,8]).reshape(2,2)

print(np.hstack((a,b)).shape == (2,4))

print(np.concatenate((a,b)))
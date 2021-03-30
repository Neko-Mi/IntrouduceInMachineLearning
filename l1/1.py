import numpy as np 

x = np.random.normal(loc=1, scale=10, size=(1000, 50))
# print(x)

m = np.mean(x, axis=0)
std = np.std(x, axis=0)
x_norm = ((x - m) / std)
# print(x_norm)

Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])

r = np.sum(Z, axis=1)
# print(np.nonzero(r > 10))

n = np.eye(3)
m = np.eye(3)
l = np.vstack((n, m))
print(l)
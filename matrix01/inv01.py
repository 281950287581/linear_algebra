import numpy as np

# from numpy.linalg import inv
#
# a = np.array([[1., 2.], [3., 4.]])
# ainv = inv(a)
# print(np.allclose(np.dot(a, ainv), np.eye(2)))
# print(np.allclose(np.dot(ainv, a), np.eye(2)))
# ainv = inv(np.matrix(a))
# print(a)
# print(inv(a))
# print(np.eye(3, dtype=int))
# print(np.eye(3, k=1))
x = np.arange(9).reshape((3,3))
print(x)
# 输出对角数组
print(np.diag(x))

print(np.diag(x, k=1))
print(np.diag(x, k=-1))
print(np.diag(np.diag(x)))
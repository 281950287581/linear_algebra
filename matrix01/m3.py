import numpy as np

a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])

print('数组 a：')
print(a)
ainv = np.linalg.inv(a)

print('a 的逆：')
print(ainv)

print('矩阵 b：')
b = np.array([[6], [-4], [27]])
print(b)

print('计算：A^(-1)B：')
# numpy.dot() 对于两个一维的数组，
# 计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
# 对于二维数组，计算的是两个数组的矩阵乘积；
x = np.dot(ainv,b)
# x = np.linalg.solve(a, b)
print(x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
# numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))
# 等价于 1*0+2*1+3*0

# numpy.matmul 函数返回两个数组的矩阵乘积

a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print(np.matmul(a,b))
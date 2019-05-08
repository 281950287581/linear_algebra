import numpy.matlib
import numpy as np

# # matlib.empty() 函数返回一个新的矩阵
# # numpy.matlib.empty(shape, dtype, order)
# print(np.matlib.empty((2,2)))
# # numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵
# print (np.matlib.zeros((2,2)))

# numpy.matlib.ones()函数创建一个以 1 填充的矩阵
# print(np.matlib.ones((2,2)))
"""
numpy.matlib.eye() 函数返回一个矩阵，
对角线元素为 1，其他位置为零
numpy.matlib.eye(n, M,k, dtype)
n: 返回矩阵的行数
M: 返回矩阵的列数，默认为 n
k: 对角线的索引
dtype: 数据类型
"""
# print(np.matlib.eye(n=3, M=4, k=0, dtype=float))
"""
numpy.matlib.identity() 函数返回给定大小的单位矩阵
单位矩阵是个方阵，从左上角到右下角的对角线
（称为主对角线）上的元素均为 1，除此以外全都为 0
"""
# 大小为 5，类型位浮点型
# print(np.matlib.identity(5, dtype=float))

"""
numpy.matlib.rand() 
函数创建一个给定大小的矩阵，数据是随机填充的
"""
# print(np.matlib.rand(3,3))

"""
矩阵总是二维的，
而 ndarray 是一个 n 维数组。
 两个对象都是可互换的
"""
i = np.matrix('1,2;3,4')
print(i)
j = np.asarray(i)

print(j)
k = np.asmatrix(j)
print(k)
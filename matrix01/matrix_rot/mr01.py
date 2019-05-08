import numpy as np

"""
rot90(m, k=1, axes=(0, 1)
m是要旋转的数组(矩阵)，k是旋转的次数，默认旋转1次，
那是顺时针还是逆时针呢？
正数表示逆时针，而k为负数时则是对数组进行顺时针方向的旋转。
"""
mat = np.array([[1, 3, 5],
                [2, 4, 6],
                [7, 8, 9]])
print(mat)
mat90 = np.rot90(mat, -1)
print(mat90)
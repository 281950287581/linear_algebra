# import numpy.matlib
# import numpy as np
#
# a = np.array([[1,2],[3,4]])
# # b = np.array([[11,12],[13,14]])
# # print(np.dot(a,b))
# print(np.linalg.det(a))
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))
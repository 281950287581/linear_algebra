from scipy.special import exp10

# 求10的x次方
# a = exp10(-1)
# print(a)

"""
再比如赫尔维茨ζζ函数公式：
scipy.special.zeta(x, q)

"""
# from scipy.special import zeta
# c = zeta(2, 1)
# print("c=", c)
"""
黎曼ζ函数可以使用scipy.special.zetac函数来实现

"""
# from scipy.special import zetac
# d = zetac(2)
# print("d=", d)

"""
polynomial子包里也有很多的知名数学公式的实现函数,
例如切比雪夫多项式
"""
import numpy.polynomial.chebyshev as chebyshev
# import numpy as np
# import numpy.linalg as linalg
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 3, 5, 4])
# # print(len(x))
# deg = len(x) - 1
# A = chebyshev.chebvander(x, deg)
# print(A)
import numpy as np
"""
poly1d可以构造一元多项式、求导、求积分以及求根等
"""
p = np.poly1d([1, 2, 1]) # 构造一元多项式
# print(p)
# print(np.polyder(p))  # 求导
# print(np.polyint(p))  # 求积分
print(np.roots([1, 2, 1])) # 求根
# np.polyval([3,0,1], 5)  # 3 * 5**2 + 0 * 5**1 + 1
print(np.polyval([1, 2, 1], 3))
import numpy as np
from scipy.integrate import quad

"""
在Scipy的integrate子包里提供了很多和积分相关的函数，
例如quad可以对一般一元函数进行积分
I=∫10(3x2+2x+1)dx=(x3+x2+x)|10=3+c
变量f是求积分的多项式 f(x)=3x2+2x+1 f(x)=3x2+2x+1，
quad函数则是求定积分函数，计算结果应该是3
"""
# f = np.poly1d([3, 2, 1])
# print(f)
# ret = quad(f, 0, 1)
# print(ret)

"""
在积分里±∞±∞用±np.inf±np.inf表示
"""
# ret = quad(lambda x: 1/x**2, -np.inf, -1)
# print(ret)

import matplotlib.pyplot as plt
# x = np.arange(-10, 0.1, 0.1)
# print(x)


# def f(x):
#     return 1/x**2
#
# y = f(x)
# print(y)
# plt.ylim(-0.1, 5)
# plt.plot(x, y)
# plt.show()

"""
如果积分的函数f带参数
I(a,b)=∫10(ax2+b)dx
那么a和b可以通过args传入quad函数

"""
# from scipy.integrate import quad
#
#
# def f(x, a, b):
#     return a * (x ** 2) + b
#
#
# ret = quad(f, 0, 1, args=(3, 1))
#
# print(ret)

"""
利用dblquad 求二重积分和tplquad求三重积分
scipy.integrate.dblquad(func, a, b, gfun, hfun, args=(), ...)
I=∫12y=0∫1−2xx=0xydydx
I=∫y=012∫x=01−2xxydydx
那么gfun(x)=lambdax:0gfun(x)=lambdax:0、
hfun(x)=lambdax:1−2∗xhfun(x)=lambdax:1−2∗x、
a=0a=0、b=0.5b=0.5。

"""
from scipy.integrate import dblquad

# lambda返回的是函数对象，也是这个函数的地址
ret = dblquad(lambda x, y: x * y, 0.0, 0.5, lambda x : 0, lambda x : 1 - 2 * x)
print(ret)
# print(1.0 / 96)
f = np.poly1d([2, -2, 0.5, 0])
print(f)
ret = quad(f, 0, 0.5)
print(ret)
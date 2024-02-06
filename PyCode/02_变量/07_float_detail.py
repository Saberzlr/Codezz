"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 01:21
@File    :   07_float_detail.py
@Author  :   Saber 
------------------------------------
"""
import sys
from decimal import Decimal 

n1 = 4.5
n2 = -3.6
print("n1 =", n1)
print("n2 =", n2)

# 浮点类型的表示形式
n3 = 5.12
n4 = .512
print("n3 =", n3)
print("n4 =", n4)

# 科学计数法形式：5.12e2，5.12E-2
n5 = 5.12e2     # 5.12*10^2
n6 = 5.12E-2    # 2.12*10^-2

print("n5 =", n5)
print("n6 =", n6)

# 浮点数的大小限制
print(sys.float_info.min)
print(sys.float_info.max)

# 浮点数精度损失解决方法
b = 8.1 / 3
print(b)    # 2.6999999999999997 存在精度损失

c = Decimal("8.1") / Decimal("3")
print(c)    # 2.7
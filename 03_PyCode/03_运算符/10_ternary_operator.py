"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 01:06
@File    :   10_ternary_operator.py
@Author  :   Saber 
------------------------------------
"""

# 得到两个数的最大值
a = 10
b = 80
max = a if a > b else b
print("max =", max) 

# 得到三个数的最大值
'''
    思路分析：
    1. a, b, c三个数
    2. 先求出 a 和 b 的最大值 max1
    3. 再求出 max1 和 b 的最大值
'''
a = 1
b = 2
c = 3
max1 = a if a > b else b
max = max1 if max1 > c else c
print("max =", max)

max = (a if a > b else b) if (a if a > b else b) > c else c
print("max =", max)
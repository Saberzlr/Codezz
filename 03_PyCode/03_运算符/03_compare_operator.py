"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 23:17
@File    :   03_compare_operator.py
@Author  :   Saber 
------------------------------------
"""

a = 9
b = 8
print(a > b)    # True
print(a >= b)   # True
print(a <= b)   # False
print(a < b)    # False
print(a == b)   # False
print(a != b)   # True
# 表示把a > b比较的结果，赋给flag
flag = a > b
print("flag =", flag) # flag = True
print(a is b)   # False
print(a is not b) # True
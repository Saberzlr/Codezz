"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 00:05
@File    :   06_and_operator_detail.py
@Author  :   Saber 
------------------------------------
"""

a = 1
b = 99

print(a and b)  # 99
# python中，()中的运算优先级最高
print((a > b) and b)    # False
print((a < b) and b)    # 99
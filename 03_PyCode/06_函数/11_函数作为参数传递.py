"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/12 17:51
@File    :   11_函数作为参数传递.py
@Author  :   Saber 
------------------------------------
"""


def f1(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val
def f2(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return num1 + num2, max_val
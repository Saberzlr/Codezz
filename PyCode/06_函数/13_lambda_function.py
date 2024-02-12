"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/13 00:07
@File    :   13_lambda_function.py
@Author  :   Saber 
------------------------------------
"""

# 编写一个函数，可以接收一个匿名函数和两个数，通过匿名函数计算，返回两个数的最大值
def f1(fun, num1, num2):
    print(f"fun类型:{type(fun)}")
    return fun(num1, num2)
'''
    1. lambda a, b: a if a > b else b 是匿名函数
    2. 不需要return,运算结果就是返回值
'''
max_val = f1(lambda a, b: a if a > b else b, 12, 10)
# test
print(max_val)
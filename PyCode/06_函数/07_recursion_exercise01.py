"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/11 23:01
@File    :   07_recursion_exercise01.py
@Author  :   Saber 
------------------------------------
"""

# 使用递归的方式求出斐波那契数列1,1,2,3,5,8,13,...给你一个整数n,求出它的值是多少?
n = int(input("请输入一个整数:"))
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(n))
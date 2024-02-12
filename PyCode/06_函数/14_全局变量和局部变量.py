"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/13 00:19
@File    :   14_全局变量和局部变量.py
@Author  :   Saber 
------------------------------------
"""

# n1就是全局变量
n1 = 100
def f1():
    # n2就是局部变量
    n2 = 200
    print(n2)
    # 可以访问全局变量n1
    print(n1)
f1()
print(n1)
# 不能访问局部变量n2
# print(n2)

n1 = 100
def f1():
    n1 = 200
    print(n1)   # 200
f1()
print(n1)       # 100

n1 = 100
def f1():
    # global关键字标明使用全局变量n1
    global n1
    n1 = 200
    print(n1)   # 200

f1()
print(n1)       # 200
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/08 13:08
@File    :   30_return.py
@Author  :   Saber 
------------------------------------
"""

# f1是一个函数
def f1():
    for i in range(1, 5):
        if i == 3:
            # return就是跳出函数
            return
            # break
            # continue
        print("i =", i)         # i = 1, i = 2
    print("结束了for...")       # 不输出

# 调用f1函数 -> 执行f1函数
f1()
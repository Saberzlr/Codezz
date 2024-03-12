"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/09 14:06
@File    :   03_return.py
@Author  :   Saber 
------------------------------------
"""

def f1():
    print("hi")

r = f1()
print("r:", r)     # None
print("r", id(r))   # None也是一种值，是空值，也有返回地址
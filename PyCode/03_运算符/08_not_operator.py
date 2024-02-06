"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 00:22
@File    :   08_not_operator.py
@Author  :   Saber 
------------------------------------
"""

a = 3
b = not (a > 3)
print(b)    # True
print(not False)    # True
print(not True)     # False
print(not 0)        # True
print(not "jack")   # False
print(not 1.88)     # False
print(not a)        # False
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 22:58
@File    :   27_break_exercise01.py
@Author  :   Saber 
------------------------------------
"""

# 1-100以内的数求和,求出当和第一次大于20的时候,当前控制循环的变量值是多少?
sum = 0
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print(i)
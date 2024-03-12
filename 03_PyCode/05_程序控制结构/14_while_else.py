"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/06 13:59
@File    :   14_while_else.py
@Author  :   Saber 
------------------------------------
"""

# while-else使用案例
i = 0
while i < 3:
    print("Saber!!!")   # 打印三句Saber!!!
    i += 1
else:
    print("i < 3 不成立 i =", i)    # 输出i < 3 不成立 i = 3

# while-else使用案例 + break
i = 0
while i < 3:
    print("Saber!!!")   # 打印两句Saber!!!之后退出while循环
    i += 1
    if i == 2:
        break
else:
    print("i < 3 不成立 i =", i)    # 不会输出
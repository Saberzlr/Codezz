"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 18:22
@File    :   24_mutiply_for_exercise.py
@Author  :   Saber 
------------------------------------
"""

# 打印输出九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if(i >= j):
            print(f"{i} * {j} = {i * j}\t", end = "")
    print("\n")
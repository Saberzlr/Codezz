"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/06 16:32
@File    :   19_while_exercise05.py
@Author  :   Saber 
------------------------------------
"""

# 输入一个整数，给出所有能构成它的结果
'''
    1. 先定义一个变量num能接收用户的输入
    2. while遍历(遍历范围:0 - num),遍历出所有能构成它的结果
    3. 输出
'''
i = 0
num = int(input("请输入一个整数:"))
while (i <= num):
    print(f"{i} + {num - i} = {num}")
    i = i + 1
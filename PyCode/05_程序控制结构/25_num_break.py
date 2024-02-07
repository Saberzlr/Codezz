"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 18:34
@File    :   25_num_break.py
@Author  :   Saber 
------------------------------------
"""

import random
'''
随机生成1-100的数,直到生成了97这个数,看看你一共用了几次?
使用random模块的randint()函数来生成随机数，该函数的语法为:
random.randint(a, b)
返回整数N满足a <= N <= b。相当于randrange(a, b+1)
'''
count = 0
while True:
    num = random.randint(1, 101)
    count += 1
    print(num, end = " ")
    if num == 97:
        break
print(f"一共用了几次{count}")
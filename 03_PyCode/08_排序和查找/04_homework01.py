"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/25 22:28
@File    :   04_homework01.py
@Author  :   Saber 
------------------------------------
"""

import random
# 随机生成10个整数(1-100的范围)保存到列表,使用冒泡排序,对其进行从大到小排序
num_list = []
for i in range(10):
    num_list.append(random.randint(1, 100))
print("排序前:", num_list)

def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
bubble_sort(num_list)
print("排序后:", num_list)
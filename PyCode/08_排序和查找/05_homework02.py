"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/25 22:30
@File    :   05_homework02.py
@Author  :   Saber 
------------------------------------
"""

import random
# 在homework01的基础上,使用二分查找,查找是否有8这个数,如果有,则返回对应的下标,如果没有,返回-1
num_list = []
for i in range(10):
    num_list.append(random.randint(1, 101))
print("排序前:", num_list)

def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
bubble_sort(num_list)
print("排序后:", num_list)

def binary_search(list, find_val):
    left = 0
    right = len(list) - 1
    find_index = -1
    while left <= right:
        mid = (left + right) //  2
        if list[mid] > find_val:
            left = mid + 1
        elif list[mid] < find_val:
            right = mid - 1
        else:
            find_index = mid
            break
    return find_index
res_index = binary_search(num_list, 89)

new_list = []
if res_index == -1:
    print("没找到:(")
else:
    new_list.append(res_index)
    for ele in new_list:
        print(f"找到了:),其下标为:{ele}")

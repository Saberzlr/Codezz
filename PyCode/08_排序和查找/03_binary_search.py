"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/25 21:28
@File    :   03_binary_search.py
@Author  :   Saber 
------------------------------------
"""

'''
思路分析:
1) 找到中间的数list[mid],与要找的值k进行比较
2) 当left <= right的时候,一直执行while循环
    1) 如果list[mid] < k => 则到list[mid]的右边进行查找
    2) 如果list[mid] > k => 则到list[mid]的左边进行查找
    3) 如果list[mid] == k => 则找到,返回对应的下标即可
3) 不断的重复上述步骤
4) 如果while循环结束也没有找到,则说明列表里没有要查找的元素
'''
list = [1, 8, 10, 89, 1000, 1234]

num = int(input("输入你要查找的数(int):"))

def binary_search(my_list, k):
    left = 0
    right = len(list) - 1
    # 定义找到数的下标
    find_index = -1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] < k:
            left = mid + 1
        elif list[mid] > k:
            right = mid - 1
        else:
            find_index = mid
            break
    return find_index

res_index = binary_search(list, num)
if res_index == -1:
    print("没找到:(")
else:
    print(f"找到了{list[res_index]},其对应的下标为{res_index}")
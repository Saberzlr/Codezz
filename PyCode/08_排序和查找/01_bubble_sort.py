"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/22 17:42
@File    :   01_bubble_sort.py
@Author  :   Saber 
------------------------------------
"""

# [24, 69, 80, 57, 13] => 使用冒泡排序实现从小到大排序
'''
冒泡排序
    每一轮排序能确定一个元素的最终位置
    n个数排序 => n - 1轮排序
    第i轮排序 => n - i次比较
思路分析:
1) 化繁为简
    1) 第一轮排序:把最大的数放到最后的位置
    第1次比较:[24, 69, 80, 57, 13]
    第2次比较:[24, 69, 80, 57, 13]
    第3次比较:[24, 69, 57, 80, 13]
    第4次比较:[24, 69, 57, 13, 80]
    for j in range(0, 4):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    2) 第二轮排序:把第二大的数放到倒数第二个的位置
    第1次比较:[24, 69, 57, 13, 80]
    第2次比较:[24, 57, 69, 13, 80]
    第3次比较:[24, 57, 13, 69, 80]
    for j in range(0, 3):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    3) 第三轮排序:把第三大的数放到倒数第三个的位置
    第1次比较:[24, 57, 13, 69, 80]
    第2次比较:[24, 13, 57, 69, 80]
    for j in range(0, 2):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    4) 第四轮排序：把第四大的数放到倒数第四个的位置
    第1次比较:[13, 24, 57, 69, 80]
    for j in range(0, 1):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
2) 先死后活
'''
num_list = [24, 69, 80, 57, 13]
print("排序前".center(32, "-"))
print(f"num_list: {num_list}")

# 先死
def bubble_sort(my_list):
    """_summary_
        对传入的列表进行排序(从小到大)
    Args:
        my_list (_type_): 传入的列表
        return: 排序好的列表
    """
    # i变量控制排序的轮数
    for i in range(4):
        # j变量控制比较的次数,同时作为比较元素的索引下标
        for j in range(4 - i):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i}轮排序的结果为: {my_list}")
    return my_list
print("排序过程".center(31, "-"))
print(f"最终排序结果为: {bubble_sort(num_list)}")

# 后活
def bubble_sort(my_list):
    """_summary_
        对传入的列表进行排序(从小到大)
    Args:
        my_list (_type_): 传入的列表
        return: 排序好的列表
    """
    # i变量控制排序的轮数
    for i in range(len(my_list) - 1):
        # j变量控制比较的次数,同时作为比较元素的索引下标
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                # 执行swap操作
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i}轮排序的结果为: {my_list}")
    return my_list
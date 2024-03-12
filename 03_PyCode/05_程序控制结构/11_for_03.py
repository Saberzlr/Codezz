"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/05 17:11
@File    :   11_for_03.py
@Author  :   Saber 
------------------------------------
"""

# for-else使用案例
nums =[1, 2, 3]
for i in nums:
    print("hello world", i)
else:
    print("没有循环数据了...")

# for循环非正常终止
nums =[1, 2, 3]
for i in nums:
    print("hello world", i)
    if i == 2:
        break;      # 中断，提前结束for循环
else:
    print("没有循环数据了...")
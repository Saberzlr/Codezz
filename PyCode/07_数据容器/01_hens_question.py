"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/13 22:41
@File    :   01_hens_question.py
@Author  :   Saber 
------------------------------------
"""

# 一个养鸡场有6只鸡,它们的体重分别是3kg、5kg、1kg、3.4kg、2kg、50kg。请问这六只鸡的总体重是多少?平均体重是多少?
'''
    思路分析:
    1) 定义6个变量来分别存储六只鸡的体重
    2) 对六只鸡的体重求和 => 总体重, 总体重 / 鸡的个数 => 平均体重
'''
hen1 = 3
hen2 = 5
hen3 = 1
hen4 = 3.4
hen5 = 2
hen6 = 50
sum = hen1 + hen2 + hen3 + hen4 + hen5 + hen6
print(f"这六只鸡的总体重是{sum}kg,平均体重是{round(sum / 6, 2)}kg")


# 使用数据容器解决
list_hens = [3, 5, 1, 3.4, 2, 50]
sum = 0
for i in list_hens:
    sum += i
    i += 1
print(f"这六只鸡的总体重是{sum}kg,平均体重是{round(sum / len(list_hens), 2)}kg")
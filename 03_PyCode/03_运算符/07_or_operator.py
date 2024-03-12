"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 00:12
@File    :   07_or_operator.py
@Author  :   Saber 
------------------------------------
"""

# or运算符的使用
# 定义一个成绩变量
score = 70
# 判断成绩是否 <= 60 或者 >= 80
if score <= 60 or score >= 80:
    print("hi~~")   # 不输出

a = 1
b = 99
print(a or b)   # 1
print((a > b) or b) # 99
print((a < b) or b) # True
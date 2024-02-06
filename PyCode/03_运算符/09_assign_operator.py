"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 00:37
@File    :   09_assign_operator.py
@Author  :   Saber 
------------------------------------
"""
# 赋值运算符
num1 = 100
i = 100
i += 100    # i = i + 100
print(i)    # 200
i -= 100    # i = i - 100
print(i)    # 100
i *= 2
print(i)    # 200

# 交换a和b
# 方法一
a = 30
b = 40
print(f"交换之前：a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"交换之后：a = {a}, b = {b}")

'''
    在python中支持一个简单的方式实现变量交换
    x, y = y, x
'''
# 方法二
a = 40
b = 50
print(f"交换之前：a = {a}, b = {b}")
a, b = b, a
print(f"交换之后：a = {a}, b = {b}")

# 方法三
a = 1
b = 2
print(f"交换之前：a = {a}, b = {b}")
a = a + b
b = a - b   # b = a + b - b = a
a = a - b   # a = a + b - a = b
print(f"交换之后：a = {a}, b = {b}")

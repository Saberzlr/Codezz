"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 01:34
@File    :   12_input_info.py
@Author  :   Saber 
------------------------------------
"""

# 可以从控制台接收用户信息[姓名、年龄、成绩]

name = input("请输入姓名:")
age = input("请输入年龄:")
score = input("请输入成绩:")

print("\n输入的信息如下")
print("name:", name)
print("age:", age)
print("score:", score)

# 从控制台接收到的数据类型是：str[字符串]
print(type(name))   # str
print(type(age))    # str
print(type(score))  # str

# 如果要对接收到的数据进行算术运算，则需要类型转换
print(10 + float(score))
# 也可以在接收数据的时候，直接转成需要的类型
age = int(input("请输入年龄:"))
print(type(age))    # int
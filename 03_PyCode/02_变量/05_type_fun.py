"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/02 23:16
@File    :   05_type_fun.py
@Author  :   Saber 
------------------------------------
"""

name = "saber"  # 字符串
age = 20        # 整型
score = 90.4    # 浮点型
gender = '男'   # 字符串
is_pass = True  # bool类型

# 查看数据的类型(本质是查看变量所指向的数据的类型)
print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(is_pass))

# type()可以直接查看具体的值(字面量)
print(f"saber的类型是{type("saber")}")
print(f"20的类型是{type(20)}")
print(f"90.4的类型是{type(90.4)}")
print(f"'男'的类型是{type('男')}")
print(f"True的类型是{type(True)}")
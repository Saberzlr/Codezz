"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 01:57
@File    :   08_bool_detail.py
@Author  :   Saber 
------------------------------------
"""

# bool类型的基本使用
num1 = 100
num2 = 200
if num1 < num2:
    print("num1 < num2")

# 将num1 > num2的结果赋给result
result = num1 > num2
if result:                             # 此处result的值是True
    print("num1 > num2")
print("result =", result)              # True
print("result的类型是:", type(result)) # <class  'bool'>
print(type(1 > -1))                    # <class  'bool'>

# 布尔类型可以和其他数据类型进行比较，比如：数字、字符串等。
# 在比较时，Python会将True是为1，False视为0
b1 = False
b2 = True

print(b1 + 10)  # 10
print(b2 + 10)  # 11

# 在Python中，非0被视为真值，0值被视为假值
if 0:
    print("hello")  # 不输出
if -1:
    print("world")  # 输出world
if 1.1:
    print("!")      # 输出world
if "你是谁":
    print("hihi")   # 输出hihi

# 课堂练习
if 1:
    print("1...")   # 输出1...
if -20:
    print("-20")    # 输出-20
if 1.1:
    print("1.1")    # 输出1.1
if -10.11:
    print("-10.11") # 输出-10.11
if "hello":
    print("hello")  # 输出hello
num1 = 0
if num1:
    print("哈哈")   # 不输出
num2 = -111.11
if num2:
    print("嘻嘻")   # 输出 嘻嘻
name = "呜呜呜"
if name:
    print(name)     # 输出 呜呜呜
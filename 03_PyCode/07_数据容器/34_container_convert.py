"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/22 15:53
@File    :   34_container_convert.py
@Author  :   Saber 
------------------------------------
"""

str_a = "hello"
list_a = ["jack", "tom", "mary"]
tuple_a = ("saber", "tim")
set_a = {"red", "black"}
dict_a = {"0001": "小倩", "0002": "黑山老妖"}

# 将指定容器转换成列表
print("-" * 32)
print(f"str_a转成列表:{list(str_a)}")
print(f"tuple_a转成列表:{list(tuple_a)}")
print(f"set_a转成列表:{list(set_a)}")
print(f"dict_a转成列表:{list(dict_a)}")

# 将指定容器转换成字符串
print("-" * 32)
print(f"list_a转成字符串:{str(list_a)}")
print(f"tuple_a转成字符串:{str(tuple_a)}")
print(f"set_a转成字符串:{str(set_a)}")
print(f"dict_a转成字符串:{str(dict_a)}")

# 将指定容器转换成元组
print("-" * 32)
print(f"list_a转成元组:{tuple(str_a)}")
print(f"tuple_a转成元组:{tuple(list_a)}")
print(f"set_a转成元组:{tuple(set_a)}")
print(f"dict_a转成元组:{tuple(dict_a)}")

# 将指定容器转换成集合
print("-" * 32)
print(f"list_a转成集合:{set(str_a)}")
print(f"tuple_a转成集合:{set(list_a)}")
print(f"set_a转成集合:{set(tuple_a)}")
print(f"dict_a转成集合:{set(dict_a)}")
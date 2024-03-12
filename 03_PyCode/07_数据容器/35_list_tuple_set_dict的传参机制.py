"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/22 16:15
@File    :   35_list_tuple_set_dict的传参机制.py
@Author  :   Saber 
------------------------------------
"""

# ---------------------------------list---------------------------------
def f1(my_list):
    print(f"② f1() my_list: {my_list} 地址是: {id(my_list)}")
    my_list[0] = "jack"
    print(f"③ f1() my_list: {my_list} 地址是: {id(my_list)}")

# test
my_list = ["tom", "mary", "saber"]
print(f"调用函数前① my_list: {my_list} 地址是: {id(my_list)}")
# 调用函数
f1(my_list)
print(f"调用函数后④ my_list: {my_list} 地址是: {id(my_list)}")
# ---------------------------------tuple---------------------------------
def f2(my_tuple):
    print(f"② f2() my_tuple: {my_tuple} 地址是: {id(my_tuple)}")
    # 元组不能修改
    # my_tuple[0] = "red"
    print(f"③ f2() my_tuple: {my_tuple} 地址是: {id(my_tuple)}")

# test
my_tuple = ("hi", "ok", "hello")
print(f"调用函数前① my_tuple: {my_tuple} 地址是: {id(my_tuple)}")
# 调用函数
f2(my_tuple)
print(f"调用函数后④ my_tuple: {my_tuple} 地址是: {id(my_tuple)}")
# ---------------------------------set---------------------------------
def f3(my_set):
    print(f"② f3() my_set: {my_set} 地址是: {id(my_set)}")
    my_set.add("红楼梦")
    print(f"③ f3() my_set: {my_set} 地址是: {id(my_set)}")

# test
my_set = {"水浒", "西游", "三国"}
print(f"调用函数前① my_set: {my_set} 地址是: {id(my_set)}")
# 调用函数
f3(my_set)
print(f"调用函数后④ my_set: {my_set} 地址是: {id(my_set)}")
# ---------------------------------dict---------------------------------
def f4(my_dict):
    print(f"② f4() my_dict: {my_dict} 地址是: {id(my_dict)}")
    my_dict['address'] = "兰若寺"
    print(f"③ f4() my_dict: {my_dict} 地址是: {id(my_dict)}")

# test
my_dict = {"name": "小倩", "age": 18}
print(f"调用函数前① my_dict: {my_dict} 地址是: {id(my_dict)}")
# 调用函数
f4(my_dict)
print(f"调用函数后④ my_dict: {my_dict} 地址是: {id(my_dict)}")
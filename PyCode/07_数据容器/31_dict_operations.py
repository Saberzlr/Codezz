"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/21 23:54
@File    :   31_dict_operations.py
@Author  :   Saber 
------------------------------------
"""

# 字典常用操作
# 定义字典
dict = {"one":1, "two":2, "three":3}


# len(d):返回字典d中的项数
print(f"dict中的项数:{len(dict)}")


# d[key]:返回d中以key为键的项。如果映射中不存在key,则会引发KeyError
print("key为three对应的value:", dict['three'])
# print("key为four对应的value:", dict["four"])


# d[key] = value:将d[key]设为value,如果key已经存在,则修改value
# 如果key没有存在,则增加key-value,会直接修改原来的字典
# 要求 修改key = 'one' 对应的value为 "第一"
dict["one"] = "第一"
print(f"dict:{dict}")
# 增加key为"four",value为4
dict["four"] = 4
print(f"dict:{dict}")


# del d[key]:将d[key]从d中移除。如果映射中不存在key则会引发KeyError
# 要求删除key为"four"的元素
del dict["four"]
print(f"dict:{dict}")


# pop(key[, default])
# 如果key存在于字典中则将其移除并返回其值,否则返回default
# 如果default未给出且key不存在于字典中,则会引发KeyError
# 要求将key为"one"的值返回,并将该元素从字典中移除
val = dict.pop("one")
print(f"val:{val}")
print(f"dict:{dict}")

val = dict.pop("four", "哈哈")
print(f"val:{val}")
print(f"dict:{dict}")

# val = dict.pop("four")


# key():返回字典所有的key
dict_keys = dict.keys()
print(f"dict_keys:{dict_keys} 类型:{type(dict_keys)}")
for k in dict_keys:
    print("key->", k)


# key in d:如果d中存在键key则返回True,否则返回False
# 要求判断字典是否有key "two"
print("two" in dict)


# clear():移除字典中所有的元素
# 要求将字典清空
dict.clear()
print(f"dict:{dict}")   
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/18 00:27
@File    :   16_str_detail.py
@Author  :   Saber 
------------------------------------
"""

str = "hi-saber"
print(id(str))
# 通过索引可以访问指定元素
print(str[3])   # s

# 不能修改元素
# str[3] = "a"  # 报错 TypeError: 'str' object does not support item assignment
str = "abc"
print(id(str))  # 指向不同的空间了
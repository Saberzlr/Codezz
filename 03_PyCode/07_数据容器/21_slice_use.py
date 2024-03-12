"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 00:31
@File    :   21_slice_use.py
@Author  :   Saber 
------------------------------------
"""

# 对字符串进行切片
str = "hello,wrold"
# 需求:截取"hello"
str_slice = str[0: 5: 1]
print(str_slice)

# 对列表进行切片
list_a = ["jack", "tom", "yoyo", "nuonuo", "saber"]
# 需求:截取["tom", "nuonuo"]
str_slice = list_a[1: 4: 2]
print(str_slice)

# 对元组进行切片
tuple_a = (100, 200, 300, 400, 500, 600)
# 需求:截取(200, 300, 400, 500)
str_slice = tuple_a[1: 5]
print(str_slice)
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 23:19
@File    :   12_tuple_operations.py
@Author  :   Saber 
------------------------------------
"""

# 元组常用操作
tuple_a = (100, 200, 300, 400, 600, 200)
print("tuple_a 列表元素个数:", len(tuple_a))
print("tuple_a 列表最大元素:", max(tuple_a))
print("tuple_a 列表最小元素:", min(tuple_a))

# 统计元组tuple_a中100出现的次数
print("200出现的次数是:", tuple_a.count(200))

# 找某个值的第一个匹配项的位置,如果找不到会报错:ValueError:x is not in tuple
print("300第1次出现在序列的位置为:", tuple_a.index(300))

print(300 in tuple_a)       # True
print(3000 in tuple_a)      # False
print(3000 not in tuple_a)  # True
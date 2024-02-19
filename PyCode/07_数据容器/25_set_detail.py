"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 14:17
@File    :   25_set_detail.py
@Author  :   Saber 
------------------------------------
"""

# 集合是由不重复元素组成的无序容器
# 不重复元素组成 -> 自动去重
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"basket:{basket}")


# 无序 -> 定义元素的顺序和取出的顺序不能保证一致
# 集合底层会按照自己的一套算法来存储和取数据,故每次取出的顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")


# 集合不支持索引
set_a = {100, 200, 300, 400, 500}
# print(set_a[0])   # 报错

# 集合不支持索引,所以对集合进行遍历不支持while,只支持for
# 使用for循环对集合进行遍历 -> 每次结果不确定一样
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for ele in basket:
    print(ele)


# 创建空集合只能用set()，不能用{},{}创建的是空字典
set_b ={}       # 创建空字典
set_c = set()   # 创建空集合
print(f"set_b:{set_b} 类型:{type(set_b)} set_c:{set_c} 类型:{type(set_c)}")
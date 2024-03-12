"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 18:19
@File    :   04_list_detail01.py
@Author  :   Saber 
------------------------------------
"""

# 如果需要一个空列表,可以通过[]或者list()方式来定义
list1 = []
list2 = list()
print(list1, type(list1))
print(list2, type(list2))

# 列表的元素可以有多个,而且数据类型没有限制,允许有重复元素,并且是有序的
list3 = [100, "jack", 4.5, True]
print(list3)

# 嵌套列表
list4 = [100, "tom", ["天龙八部", "笑傲江湖", 300]]
print("list4=", list4)

# 索引也可以从尾部开始,最后一个元素的索引为-1,往前一位为-2,以此类推
list3 = [100, "jack", 4.5, True]
print(list3[-1])    # True
print(list3[-2])    # 4.5

# 通过 列表[索引] = 新值 对数据进行更新，使用 列表.append(值)方法来添加元素
list_a = ["天龙八部", "笑傲江湖"]
print("list_a:", list_a)
list_a[0] = "雪山飞狐"
print("list_a:", list_a)
list_a.append("倚天屠龙记")
print("list_a:", list_a)
del list_a[1]
print("list_a:", list_a)
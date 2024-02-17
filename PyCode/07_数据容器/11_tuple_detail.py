"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 22:44
@File    :   11_tuple_detail.py
@Author  :   Saber 
------------------------------------
"""

# 如果需要一个空元组，可以通过()，或者tuple()方式来定义
tuple_a = ()
tuple_b = tuple()
print(f"tuple_a内容是{tuple_a} 类型是{type(tuple_a)}")
print(f"tuple_b内容是{tuple_b} 类型是{type(tuple_b)}")

# 元组的元素可以有多个，而且数据类型没有限制(甚至可以嵌套元组)，允许有重复元素，并且是有序的。
tuple_c = (100, "jack", 4.5, True, "jack")
print(tuple_c)
# 嵌套元组
tuple_d = (100, "tom", ("天龙八部", "笑傲江湖", 300))
print(tuple_d)


# 元组是不可变序列
tuple_e = (1, 2.1, 'Saber')
# tuple_e[2] = 'python'


# 可以修改元组内列表(list)的内容(包括：修改、增加、删除)
tuple_f = (1, 2.1, 'Saber', ["jack", "tom", "mary"])
# 访问元组中list及其元素
print(tuple_f[3])
print(tuple_f[3][0])
# 修改
tuple_f[3][0] = "python"
print(f"tuple_f内容是{tuple_f}")
# 删除
del tuple_f[3][0]
print(f"tuple_f内容是{tuple_f}")
# 增加
tuple_f[3].append("smith")
print(f"tuple_f内容是{tuple_f}")

# 索引也可以从尾部开始，最后一个元素的索引是-1，往前一位为-2，以此类推
tuple_g = (1, 2.1, 'Saber', ["jack", "tom", "mary"])
print(tuple_g[-2])


# 定义只有一个元素的元组，需要带上逗号
tuple_h = (100,)
print(f"tuple_h的类型是{type(tuple_h)}")
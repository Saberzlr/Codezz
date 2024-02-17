"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 18:19
@File    :   05_list_detail02.py
@Author  :   Saber 
------------------------------------
"""

# 列表的元素是可以修改的,修改后,列表变量的指向地址不变,只是数据内容变化
list1 = [1, 2.1, 'Saber']
print(f"list1:{list1} 地址:{id(list1)} || {list1[2]}的地址:{id(list1[2])}")
list1[2] = 'python'
print(f"list1:{list1} 地址:{id(list1)} || {list1[2]}的地址:{id(list1[2])}")

# 扩展 --- 列表在赋值时的特点
list1 = [1, 2.1, 'Saber']
list2 = list1
list2[0] = 500
print("list2 =", list2)     # [500, 2.1, Saber]
print("list1 =", list1)     # [500, 2.1, Saber]
# 与下面的变量相区分
a = 10
b = a
print(f"b = {b}, address:{id(b)}")  # b = 10, address:140724512635608
b = 50
print(f"b = {b}, address:{id(b)}")  # b = 50, address:140724512636888

# 扩展 --- 列表在函数传参时的特点
def f1(a):
    a[0] = 100
    print("a的id:", id(a))

list2 = [1, 2.1, 200]
print("list2的id:", id(list2))
f1(list2)
print("list2:", list2)
# 与下面的变量相区分
def f2(b):
    b = 10
    print("b =", b)

a = 100
print("a =", a)
f2(a)
print("a =", a)
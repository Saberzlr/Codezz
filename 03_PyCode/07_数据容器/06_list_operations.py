"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 18:45
@File    :   06_list_operations.py
@Author  :   Saber 
------------------------------------
"""

# 列表常用操作
list_a = [100, 200, 300, 400, 600]
print("list_a 列表元素个数:", len(list_a))
print("list_a 列表最大元素:", max(list_a))
print("list_a 列表最小元素:", min(list_a))

# 在list_a列表后添加900
list_a.append(900)
print("list_a:", list_a)

# 统计列表list_a中100出现的次数
print("100出现的次数是:", list_a.count(100))

# 用新列表扩展原来的列表
list_b = [1, 2, 3]
list_a.extend(list_b)
print("list_a:", list_a)

# 找某个值的第一个匹配项的位置,如果找不到会报错:ValueError
print("300第1次出现在序列的位置为:", list_a.index(300))

# 翻转list_a
list_a.reverse()
print("list_a翻转后为:", list_a)

# 将666插入到index为1的位置
list_a.insert(1, 666)
print("list_a:", list_a)
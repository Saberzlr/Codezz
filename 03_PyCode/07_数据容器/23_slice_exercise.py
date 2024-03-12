"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 01:06
@File    :   23_slice_exercise.py
@Author  :   Saber 
------------------------------------
"""

'''
定义列表list_name = ["Jack", "Lisa", "Saber", "Paul", "Smith", "Kobe"]
1) 取出前三个名字
2) 取出后三个名字,并保证原来顺序
'''
list_name = ["Jack", "Lisa", "Saber", "Paul", "Smith", "Kobe"]
# 取出前三个名字
list_slice01 = list_name[:3:]
print("取出前三个名字:", list_slice01)
# 取出后三个名字,并保证原来顺序
list_slice02 = list_name[:-4:-1]
list_slice02.reverse()
print("取出后三个名字:", list_slice02)
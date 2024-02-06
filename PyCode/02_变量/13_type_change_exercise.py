"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 20:41
@File    :   13_type_change_exercise.py
@Author  :   Saber 
------------------------------------
"""

# 课后练习
i = 10
j = float(i)
print(type(i))  # int
print(type(j))  # float

i = j + 1
print(type(i))  # float
print(type(j))  # float

print(i)        # 11.0
print(int(i))   # 11
print(type(i))  # float
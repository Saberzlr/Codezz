"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 19:15
@File    :   07_list_create.py
@Author  :   Saber 
------------------------------------
"""

print([ele * 2 for ele in range(1, 5)])
print([ele + ele for ele in "Saber"])

# 要求生成一个列表:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([ele * ele for ele in range(1, 11)])
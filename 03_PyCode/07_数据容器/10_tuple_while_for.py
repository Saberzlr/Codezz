"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/18 00:20
@File    :   10_tuple_while_for.py
@Author  :   Saber 
------------------------------------
"""

# 通过for循环来遍历元组
tuple_color = ('red', 'blue', 'yellow', 'green', 'white', 'black')
for ele in tuple_color:
    print(ele)
    
# 通过while循环来遍历元组
tuple_color = ('red', 'blue', 'yellow', 'green', 'white', 'black')
i = 0
while(True):
    print(tuple_color[i])
    i += 1
    if i == 6:
        break
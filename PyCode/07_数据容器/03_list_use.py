"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/14 01:57
@File    :   03_list_use.py
@Author  :   Saber 
------------------------------------
"""

list2 = ['red', 'blue', 'yellow', 'white', 'black']
print(list2)
print("第三个元素是:", list2[2])


# 列表遍历
'''
1. 先定义变量index = 0表示从第一个元素开始取出
2. 决定列表list_color的个数6,使用内置函数len(列表),可以返回元素个数
3. 每取出一个就输出/根据自己的业务处理
'''
list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']
index = 0
while index < len(list_color):
    print(list_color[index])
    index += 1

# for循环实现
list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']
for i in list_color:
    print(i)
    index += 1
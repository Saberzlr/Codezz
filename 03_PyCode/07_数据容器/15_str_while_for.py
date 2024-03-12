"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/18 00:20
@File    :   15_str_while_for.py
@Author  :   Saber 
------------------------------------
"""

# 使用while和for循环遍历字符串
str_b = "hi-saber"
# while循环遍历
i = 0
while i < len(str_b):
    print(f"第{i + 1}个元素是->{str_b[i]}")
    i += 1
print("------------------------------")
print("-" * 30)
# for循环遍历
for ele in str_b:
    print(ele)
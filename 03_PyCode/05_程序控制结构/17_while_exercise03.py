"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/06 14:12
@File    :   17_while_exercise03.py
@Author  :   Saber 
------------------------------------
"""

# 不断输入姓名，直到输入"exit"为止
name = ""
while name != "exit":
    name = input("请输入姓名:")
    print("输入的内容是:", name)
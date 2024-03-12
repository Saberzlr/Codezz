"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 19:31
@File    :   08_list_exercise01.py
@Author  :   Saber 
------------------------------------
"""

# 循环从键盘输入5个成绩,保存到列表
list_score = []
for i in range(5):
    list_score.append(float(input("请输入你的成绩(5次):")))
print(list_score)
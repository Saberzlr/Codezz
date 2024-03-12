"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/05 12:42
@File    :   07_nested_if_example1.py
@Author  :   Saber 
------------------------------------
"""

# 参加歌手比赛，如果初赛成绩大于8.0则进入决赛，否则提示淘汰。并且根据性别提示进入男子组或女子组。输入成绩和性别，进行判断和输出信息。
grade = float(input("请输入歌手的成绩:"))
if grade > 8.0:
    gender = input("请输入歌手性别:")
    if gender == "男":
        print("进入男子组!")
    elif gender == "女":
        print("进入女子组!")
    else:
        print("性别不合法!")
else:
    print("你被淘汰了!")
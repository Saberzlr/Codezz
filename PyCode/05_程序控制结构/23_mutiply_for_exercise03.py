"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 13:46
@File    :   23_mutiply_for_exercise03.py
@Author  :   Saber 
------------------------------------
"""

'''
统计三个班的成绩情况,每个班有5名同学,要求完成:
1) 求出各个班的平均分和所有班级的平均分,学生的成绩从键盘输入
2) 统计三个班及格人数

化繁为简:
1. 统计1个班的成绩情况,求出1个班的平均分
2. 统计3个班的成绩情况,求出各个班的平均分、所有班级的平均分和及格人数
'''

# 统计1个班的成绩情况,求出1个班的平均分
count = 0
sum = 0.0
for j in range(1, 6):
    score = float(input("请输入学生的成绩:"))
    if score >= 60.0:
        count += 1
    sum += score
    avg = sum / 5.0
print(f"class1的平均分为{avg},及格人数为{count}个")

# 统计3个班的成绩情况,求出各个班的平均分、所有班级的平均分和及格人数
count = 0       # 计数器,用来统计及格人数
sum = 0.0       # 统计班级总分
total = 0.0     # 统计所有班级的总平均分
# 外层循环用来统计多个班级
for i in range(1, 4):
    sum = 0.0   # 一个班统计完后,sum要清零
    # 内层循环用来统计一个班级,循环多次,处理多个学生
    for j in range(1, 6):
        score = float(input(f"请输入第{i}个班的第{j}个学生的成绩:"))
        if score >= 60.0:
            count += 1
        sum += score
        avg = sum / 5.0
        total += avg
    print(f"class{i}的平均分为{avg}")
total_avg = total / 3
print(f"所有班级的平均分为{total_avg},及格人数为{count}个")


# 统计3个班的成绩情况,求出各个班的平均分、所有班级的平均分和及格人数
class_num = 0   # 记录班级个数
count = 0       # 计数器,用来统计及格人数
sum = 0.0       # 统计班级总分
total = 0.0     # 统计所有班级的总平均分
class_num = int(input("请输入共有几个班级:"))
stu_num = int(input("请输入该班共有几个学生:"))
# 外层循环用来统计多个班级
for i in range(1, class_num + 1):
    sum = 0.0   # 一个班统计完后,sum要清零
    # 内层循环用来统计一个班级,循环多次,处理多个学生
    for j in range(1, stu_num + 1):
        score = float(input(f"请输入第{i}个班的第{j}个学生的成绩:"))
        if score >= 60:
            count += 1
        sum += score
        avg = sum / stu_num
    print(f"class{i}的平均分为{avg}")
    total += avg
total_avg = total / class_num
print(f"所有班级的平均分为{total_avg},及格人数为{count}个")
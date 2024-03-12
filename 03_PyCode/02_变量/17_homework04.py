"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 20:56
@File    :   17_homework04.py
@Author  :   Saber 
------------------------------------
"""

# 编程实现如下效果
'''
    姓名    年龄    成绩    性别    爱好
    xx      xx     xx      xx      xx
要求：
1) 用变量将姓名、年龄、成绩、性别、爱好存储
2) 使用+
3) 添加适当的注释
4) 添加转义字符，使用一条语句输出
'''

name = "Saber"
age = 18
score = 99.9
gender = "女"
hobby = "参加圣杯战争"
# 输出信息
print("姓名\t年龄\t成绩\t性别\t爱好\n" 
    + name + "\t" + str(age) 
    + "\t" + str(score) + "\t" + gender + "\t" + hobby)
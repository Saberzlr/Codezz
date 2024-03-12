"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 22:01
@File    :   05_if_elif.py
@Author  :   Saber 
------------------------------------
"""

'''
    小头儿子参加python考试，他和大头爸爸达成承诺：
    如果成绩为100分，奖励一辆BMW；
    成绩为(80, 99]时，奖励一台iphone13；
    当成绩为[60,80]时，奖励一个ipad；
    其他情况时，什么奖励也没有。
    请从键盘输入小头儿子的期末成绩，并加以判断
'''
score = float(input("请输入小头儿子的成绩:"))
# if score >= 0 and score <= 100:
if 0 <= score <= 100:
    if score == 100:
        print("奖励一辆BMW!")
    # elif score > 80 and score <= 99:
    elif 80 < score <= 99:
        print("奖励一台iphone13!")
    # elif score >= 60 and score <= 80:
    elif 60 <= score <=80:
        print("奖励一个iPad!")
    else:
        print("考这么差,还想要奖励???")
else:
    print("你输入的成绩不合法:(")


# 分析下面代码的输出结果
b = True
if b == False:
    print("a")      # 不输出
elif b:
    print("b")      # 输出b，并退出if语句
elif not b:
    print("c")      # 不输出也不执行
else:
    print("d")      # 不输出也不执行
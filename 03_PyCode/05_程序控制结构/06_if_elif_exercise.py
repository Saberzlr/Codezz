"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 22:19
@File    :   06_if_elif_exercise.py
@Author  :   Saber 
------------------------------------
"""

'''
    女方家长要嫁女儿，要提出条件：身高：180cm；财富1000万以上；帅：是。条件从控制台输入。
    如果这三个条件同时满足，则："我一定要嫁给他!"
    如果三个条件有为真的情况，则:"嫁吧,比上不足,比下有余。"
    如果三个条件都不满足，则:"不嫁!"
'''

height = float(input("请输入你的身高(cm):"))
money = float(input("请输入你的财产(千万元):"))
handsome = int(input("你觉得你自己刷吗(帅=>1;不帅=>0)?"))

if height >= 180 and money >= 1000 and handsome:
    print("我一定要嫁给他!")
elif height >= 180 or money >= 1000 or handsome:
    print("嫁吧,比上不足,比下有余。")
else:
    print("不嫁!")
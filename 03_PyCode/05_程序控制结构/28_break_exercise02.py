"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 23:04
@File    :   28_break_exercise02.py
@Author  :   Saber 
------------------------------------
"""

# 实现登录验证,有三次机会,如果用户名为"Saber",密码为"666",则提示登录成功,否则提示还有几次机会,使用for+break完成
for i in range(1, 4):
    usrname = input("请输入用户名:")
    passwd = input("请输入密码:")
    if usrname == "Saber" and passwd == "666":
        print("登录成功!")
        break
    else:
        print(f"用户名或密码错误,还有{3 - i}次机会")
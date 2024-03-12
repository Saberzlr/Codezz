"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/08 22:34
@File    :   01_calculate_question.py
@Author  :   Saber 
------------------------------------
"""


# 输入两个数,再输入一个运算符(+,-,*,/),得到结果
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
optr = input("请输入一个运算符(+ - / *):")
res = 0.0
if optr == "+":
    res = num1 + num2
elif optr == "-":
    res = num1 - num2
elif optr == "*":
    res = num1 * num2
elif optr == "/":
    res = num1 / num2
else:
    print("输入的运算符不合法!")
print(num1, optr, num2, "=", res)

# 如果还有这样的需求,如果复制代码,会比较冗杂,不利于代码的维护 => 使用函数
def oper(num1, num2, optr):
    if optr == "+":
        return num1 + num2
    elif optr == "-":
        return num1 - num2
    elif optr == "*":
        return num1 * num2
    elif optr == "/":
        return num1 / num2
    else:
        print("输入的运算符不合法!")
        
res = oper(2, 3, "/")
print(res)
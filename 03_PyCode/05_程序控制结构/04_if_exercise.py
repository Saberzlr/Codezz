"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 21:06
@File    :   04_if_exercise.py
@Author  :   Saber 
------------------------------------
"""

x = 4
y = 1
if x > 2:
    if y > 2:
        print(x + y)    # 不输出
    print("Saber")      # 输出Saber
else:
    print("x is", x)    # 不输出

# 编写程序，定义2个整数变量并赋值，判断两数之和，如果大于等于50，打印"hello world!"
num1 = 20
num2 = 30
sum = num1 + num2
if sum >= 50:
    print("hello world!")

# 编写程序，定义2个float型变量并赋值，如果第一个数大于10.0，且第2个数小于20.0，打印两数之和
var1 = 20.5
var2 = 15.5
if var1 > 10.0 and var2 < 20.0:
    print(f"{num1} + {num2} = {num1 + num2}")

# 定义两个变量int类型，判断二者的和，是否能被3整除又能被5整除，打印提示信息
num1 = 10
num2 = 20
sum = num1 + num2
if sum % 3 == 0 and sum % 5 == 0:
    print("能被3和5都整除")
else:
    print("不能被3和5都整除")

# 判断一个年份是否是闰年，闰年的条件是符合下面二者之一：(1)年份能被 4整除，但不能被100整除(2)能被400整除
year = int(input("请输入年份:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 19:43
@File    :   10_type_change.py
@Author  :   Saber 
------------------------------------
"""

# python根据该变量使用的上下文在运行时决定的
var1 = 10
print(type(var1))
var1 = 1.1
print(type(var1))
var1 = "saber!!!"
print(type(var1))

# 在运算的时候，数据类型会向高精度自动转换,float精度高于int
var2 = 10
var3 = 1.2
var4 = var2 + var3  # 11.2 float
print(f"var2的类型是：{type(var2)}\nvar2的类型是：{type(var3)}\nvar4的类型是：{type(var4)}")
var2 = var2 + 0.1   # 10.1 float
print(f"var2的类型是：{type(var2)}")
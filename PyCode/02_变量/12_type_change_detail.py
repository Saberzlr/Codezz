"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 20:15
@File    :   12_type_change_detail.py
@Author  :   Saber 
------------------------------------
"""

# 显式类型转换注意事项
# 不管什么值的int、float都可以转换为str，str(x)将对象x转换为字符串
n1 = 100
n2 = 103.45
print(type(str(n1)))
print(type(str(n2)))

# int转成float时，会增加小数部分；float转成int时，会去掉小数部分
n3 = float(n1)
n4 = int(n2)
print(n3)   # 100.0
print(n4)   # 103

# str转int，float时，使用int(x), float(x)将对象x转换为int/float
n5 = "12.3"
print(float(n5))    # 12.3
# print(int(n5))      # 报错

# 在将str类型转成基本数据类型时，要确保str值能够转成有效的数据，比如："123"可以转成一个整数，但是不能把"hello"转成一个整数，如果格式不正确，程序会报错"ValueError"，程序就会终止
n6 = "hello"
# print(float(n6))    # 报错
# print(int(n6))      # 报错

# 强制转换后，并不会影响原变量的数据类型
i = 10
j = float(i)
print("i的值为:", i, "\ni的类型为:", type(i))   # 10 int
print("i的值为:", j, "\ni的类型为:", type(j))   # 10.0 float

k = str(i)
print("i的值为:", i, "\ni的类型为:", type(i))   # 10 int
print("i的值为:", k, "\ni的类型为:", type(k))   # "10" str
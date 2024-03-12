"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/11 16:32
@File    :   05_字符串和数值类型的传参机制.py
@Author  :   Saber 
------------------------------------
"""

# 定义函数f1
# 数值类型的传参机制
def f1(a):
    print(f"f1() a的值:{a} 地址是:{id(a)}")
    a += 1
    print(f"f1() a的值:{a} 地址是:{id(a)}")

a = 10
print(f"调用f1()前 a的值:{a} 地址是:{id(a)}")
f1(a)
print(f"调用f1()后 a的值:{a} 地址是:{id(a)}")

# 定义函数f2
# 字符串类型的传参机制
def f2(name):
    print(f"f2() name的值:{name} 地址是:{id(name)}")
    name = "Saber"
    print(f"f2() name的值:{name} 地址是:{id(name)}")
print("--------------------------")
name = "tom"
print(f"调用f2()前 name的值:{name} 地址是:{id(name)}")
f2(name)
print(f"调用f2()后 name的值:{name} 地址是:{id(name)}")
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/12 17:55
@File    :   12_function_arg.py
@Author  :   Saber 
------------------------------------
"""

def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val

def f1(fun, num1, num2):
    """_summary_
    调用fun返回num1和num2的最大值
    Args:
        fun (_type_): 表示接收一个函数
        num1 (_type_): 传入的数字1
        num2 (_type_): 传入的数字2

    Returns:
        _type_: 最大值
    """
    return fun(num1, num2)

def f2(fun, num1, num2):
    """_summary_
    调用fun返回num1和num2的最大值,同时返回两个数的和
    Args:
        num1 (_type_): 传入的数字1
        num2 (_type_): 传入的数字2

    Returns:
        _type_: 两个数的和,最大值
    """
    return num1 + num2, fun(num1, num2)

# test
print(f1(get_max_val, 35, 39))
x, y = f2(get_max_val, 20, 30)
print("x =", x, "y =", y)


# f3接收多个函数作为参数传入
def f3(my_fun, num1, num2, my_fun2):
    return my_fun2(num1, num2), my_fun(num1, num2)

# 定义一个函数，可以返回两个数的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val

# 定义函数，可以返回两个数的和
def get_sum(num1, num2):
    return num1 + num2

print(f3(get_max_val, 130, 190, get_sum))
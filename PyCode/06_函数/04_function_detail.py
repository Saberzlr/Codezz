"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/09 14:51
@File    :   04_function_detail.py
@Author  :   Saber 
------------------------------------
"""

def cry():
    print("cry()...hi...")
def cry():
    print("cry1()...hi...")


# 这个cry会默认就近原则，即第二个cry()
cry()	# 会输出cry1()...hi...

# 如果同一个文件，出现两个函数名相同的函数，则以就近原则进行调用
def cry(n):
    print("cry()...hi...", n)
def cry():
    print("cry1()...hi...")

# 这个cry会默认就近原则，即第二个cry()
cry()	# 会输出cry1()...hi...
# cry(10)	# 会报错


# 调用函数时，根据函数定义的参数位置来传递参数，这种传参方式就是位置参数，传递的实参和定义的形参顺序和个数必须一致，同时定义的形参，不用指定数据类型，会根据传入的实参决定
def car_info(name, price, color):
    print(f"name->{name} price->{price} color->{color}")

# car_info("宝马", 500000, "blue", 11)    # 会报错TypeError，形参和实参个数不一致
car_info("宝马", 500000, "blue")


# 函数可以有多个返回值，返回数据类型不受限制
def f2(n1, n2):
    return n1 + n2, n1 - n2
r1, r2 = f2(10, 20)
print("r1 =", r1, "r2 =", r2)


# 函数支持关键字参数
def book_info(name, price, author, amount):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")

# 通常调用方式 -> 一一对应
book_info("红楼梦", 60, "曹雪芹", 30000)

# 关键字参数
print("-------------关键字参数-------------")
book_info(name="红楼梦", price = 60, amount = 30000, author = "曹雪芹")
book_info("红楼梦", 60, amount = 30000, author = "曹雪芹")

print("\n")
# 函数支持默认参数/缺省参数
def book_info2(name ='<<thinking in python>>', price = 66.8, author = '龟叔', amount = 1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")
# 不报错
def book_info2(name, price, author = '龟叔', amount = 1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")
# 报错
# def book_info2(name ='<<thinking in python>>', price, author = '龟叔', amount = 1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")
# 报错
# def book_info2(name ='<<thinking in python>>', price = 66.8, author, amount):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")
# 调用测试
# book_info2()                    # 以默认值为主
# book_info2('<<study python>>')  # 以给定的实参为主

# 函数支持可变参数/不定长参数
# 计算多个数的和，但是不知道具体是多少个数 -> *[表示 0 到 多]
def sum(*args): # args->[1, 2, 3, 100]
    print(f"args->{args} 类型是->{type(args)}")
    total = 0
    # 对args进行遍历，即对元组tuple进行遍历
    for i in args:
        total += i
    return total
# 调用测试
res = sum(1, 2, 3, 100)
print(f"res->{res}")

res = sum(1, 2, 3, 100, 5, 6, 100)
print(f"res->{res}")

res = sum()
print(f"res->{res}")

# 我们需要接收一个人的信息，但是有哪些信息是不确定的，就可以使用关键字可变参数
def person_info(**args):
    print(f"args->{args} 类型->{type(args)}")
    # 遍历args，是一个字典，下面的arg_name就是取出各个参数名
    # args[arg_name]就是取出参数值
    for arg_name in args:
    # for arg_name in {'name': 'Saber', 'age': 18, 'email': 'Saber@qq.com'}:
        print(f"参数名->{arg_name} 参数值->{args[arg_name]}")

# 测试
person_info(name = "Saber", age = 18, email = "Saber@qq.com", gender = "女")
person_info(name = "Saber", age = 18, email = "Saber@qq.com", gender = "女", address = "大不列颠")
person_info()
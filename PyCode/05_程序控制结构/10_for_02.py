"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/05 16:52
@File    :   10_for_02.py
@Author  :   Saber 
------------------------------------
"""

'''
range函数的解读:
class range(stop)
class range(start, stop, step = 1)
1. 虽然被称为函数,但range实际上是一个不可变的序列类型
2. range默认增加的步长step是1,也可以指定,start默认是0
3. 通过list()可以查看range()生成的序列包含的数据
4. range()生成的数据是前闭后开  range(1, 5) => 1 2 3 4
'''

# 生成一个[1, 2, 3, 4, 5]
r1 = range(1, 6)
print("r1 =", list(r1))
# 生成一个[0, 1, 2, 3, 4, 5]
# r2 = range(0, 6)
r2 = range(6)
print("r2 =", list(r2))
# 生成一个[1, 3, 5, 7, 9]
r3 = range(1, 10, 2)
print("r3 =", list(r3))
# 使用for + range方式输出10句 "hello,python"
# for i in range(1, 11):
for i in range(10):
    print("hello,python")
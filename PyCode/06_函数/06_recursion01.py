"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/11 18:18
@File    :   06_recursion01.py
@Author  :   Saber 
------------------------------------
"""

def test(n):
    if n > 2:
        test(n - 1)
    print("n =", n)
test(4)

def test(n):
    if n > 2:
        test(n - 1)
    else:
        print("n =", n)
test(4)
# test(4) 4 > 2 => test(3) 3 > 2 => test(2) 2 > 2(x) => n = 2

# 阶乘，当执行fac(4)时，返回值是多少
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n
# 执行
print(fac(4))
# fac(4) 4 != 1 => fac(3) * 4 3 != 1 => fac(2) * 3 2 != 1 => fac(1) * 1 1 == 1 => fac(1) = 1
# fac(1) = 1 => fac(2) = fac(1) * 2 = 2 => fac(3) = fac(2) * 3 = 2 * 3 = 6 => fac(4) = fac(3) * 4 = 6 * 4 = 24
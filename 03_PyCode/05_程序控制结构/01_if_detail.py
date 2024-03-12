"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/04 19:18
@File    :   01_if_detail.py
@Author  :   Saber 
------------------------------------
"""

# 会输出ok1和ok2
if 4 > 1:
    print("ok1")
    print("ok2")

# 只会输出hello3
if 4 < 1:
    print("hello1")
    print("hello2")
print("hello3")

# 最短的缩进对较长的有包含关系，缩进前后没有要求
# 每个代码块应具有相同的缩进长度（TAB或者相同个数的空格）
# 第24行代码包含第25 - 27行代码，第27行代码包含第28行代码
if 100 > 20:
    print("ok3")
    print("ok4")
    if 8 > 2:
        print("ok5")
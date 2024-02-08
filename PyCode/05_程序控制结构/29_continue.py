"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/08 12:24
@File    :   29_continue.py
@Author  :   Saber 
------------------------------------
"""

i = 1
while i <= 4:
    i += 1
    if i == 3:
        continue
    print("i =", i) # i = 2, i = 4, i = 5

# 分析下面的代码输出结果是什么?
for i in range(13):
    if i == 10:
        continue
    print("i =", i)

for i in range(2):
    for j in range(1, 4):
        if j == 2:
            continue
        print("i =", i, "j =", j)
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/07 19:04
@File    :   26_break_detail.py
@Author  :   Saber 
------------------------------------
"""

# 它会终结最近的外层循环，如果循环有可选的else子句，也会跳过该子句
count = 0
while True:
    print("saber")  # 打印saber
    count += 1
    if count == 3:
        break
    while True:
        print("OK while")   # OK while
        break
else:
    print("Hello,while")

# 如果一个for循环被break所终结，该循环的控制变量会保持当前值
nums = [1, 2, 3, 4, 5, 6]
for i in nums:
    if i > 3:
        break
print("i =", i)
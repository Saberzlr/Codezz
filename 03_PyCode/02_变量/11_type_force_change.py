"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 20:00
@File    :   11_type_force_change.py
@Author  :   Saber 
------------------------------------
"""

# 显式转换案例
i = 10
j = float(i)
print(f"j的类型为{type(j)}\nj的值为{j}")    # float 10.0

k = str(i)
print(f"k的类型为{type(k)}\nj的值为{k}")    # str "10"
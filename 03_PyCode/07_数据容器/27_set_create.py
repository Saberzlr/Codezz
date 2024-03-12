"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 17:24
@File    :   27_set_create.py
@Author  :   Saber 
------------------------------------
"""

set1 = {ele * 2 for ele in range(1,5)}
print("set1:", set1)
set2 = {ele + ele for ele in "Saber"}
print("set2:", set2)
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/05 13:50
@File    :   09_for_01.py
@Author  :   Saber 
------------------------------------
"""

# for循环
# 定义一个列表
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums, type(nums)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>

# 循环输出十句话
for i in nums:
    print("Excalibur!!!", i)
print("---------------------")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Excalibur!!!", i)

# 内存驻留机制
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums, id(nums), nums[0], id(nums[0]))
print(id(1))
print(nums, id(nums), nums[1], id(nums[1]))
print(nums, id(nums), nums[2], id(nums[2]))

nums2 = [1, 2]
print(nums2, id(nums2), nums2[0], id(nums2[0]))
print(nums2, id(nums2), nums2[1], id(nums2[1]))
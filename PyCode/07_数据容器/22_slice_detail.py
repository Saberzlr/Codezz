"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 00:43
@File    :   22_slice_detail.py
@Author  :   Saber 
------------------------------------
"""

# 序列[起始索引:结束索引:步长]，起始索引如果不写，默认为0，结束索引如果不写，默认截取到结尾，步长如果不写，默认为1
str = "hello,saber"

str_slice01 = str[:5:1]
print("str_slice01->", str_slice01)     # hello
str_slice02 = str[1::1]
print("str_slice02->", str_slice02)     # ello,saber
str_slice03 = str[::1]
print("str_slice03->", str_slice03)     # hello,saber
str_slice04 = str[2:5:]
print("str_slice04->", str_slice04)     # llo


# 切片语法：序列[起始索引:结束索引:步长]，步长为负数，表示反向取，同时起始索引和结束索引也要反向标记。
str = "123456"
str_slice05 = str[-1::-1]
print("str_slice05->", str_slice05)     # 654321

str_slice06 = str[-1:-6:-1]
print("str_slice06->", str_slice06)     # 65432


# 切片操作并不会影响原序列，而是返回了一个序列
str = "ABCD"
str_slice07 = str[1:3:1]
print("str->",str, "str_slice07->", str_slice07)     # str->ABCD str_slice07->BC
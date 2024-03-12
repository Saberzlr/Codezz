"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/18 21:27
@File    :   17_str_operations.py
@Author  :   Saber 
------------------------------------
"""

# 字符串的常用操作
str_names = "jack tom mary saber nuonuo tome jack"


# 求字符串的长度
print(f"{str_names} 包含 {len(str_names)} 个字符")


# 将"jack"替换成"杰克",只替换一个
'''
    说明:返回字符串的副本 表示原来的字符串不变,而是返回一个新的字符串
'''
# 1表示替换一个,不写就表示全部替换(默认)
str_names_new = str_names.replace("jack", "杰克", 1)
print(str_names, id(str_names))             # jack tom mary saber nuonuo tome jack
print(str_names_new, id(str_names_new))     # 杰克 tom mary saber nuonuo tome jack


# 对str_names按照" "进行分割
str_names_split = str_names.split(" ")
print(f"str_names_split内容是: {str_names_split} 类型是: {type(str_names_split)}")  #  ['jack', 'tom', 'mary', 'saber', 'nuonuo', 'tome', 'jack']  <class 'list'>
print(f"str_names内容是: {str_names}") # jack tom mary saber nuonuo tome jack


# 统计tom在字符串出现了几次
print("tom在字符串出现的次数为:", str_names.count("tom"))


# 找出jack在字符串中第一个匹配项的索引位置
print(f"jack第一次出现的索引的是: {str_names.index("jack")}")
print(f"tom第一次出现的索引的是: {str_names.index("tom")}")


# 除去字符前后的空格,或者去掉指定的某些字符
# 要求去除str_names前后的空格
str_names = " jack "
str_names_strip = str_names.strip(" ")
print("str_names_strip:", str_names_strip)
print("str_names:", str_names)

str_names = "123s123aber321"
str_names_strip = str_names.strip("132")
print("str_names_strip:", str_names_strip)
print("str_names:", str_names)


# 将字符串全部改为小写 -> 不会影响原来的字符串
str_names = "SABEr"
str_names_low = str_names.lower()
print("str_names_low:", str_names_low)


# 将字符串全部改为大写 -> 不会影响原来的字符串
str_names_upper = str_names.upper()
print("str_names_upper:", str_names_upper)
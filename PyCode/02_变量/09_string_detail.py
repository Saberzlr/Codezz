"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 02:36
@File    :   09_string_detail.py
@Author  :   Saber 
------------------------------------
"""

# 字符串使用注意事项

# 使用引号('或")包括起来，创建字符串
str1 = 'tom说："hello"'
str2 = "tom说：\"hello\""
print(str1)
print(str2)
str3 = "jack说：'hi'"
str4 = 'jack说：\'hi\''
print(str3)
print(str4)
print(f"str2的类型是{type(str2)}")

# 通过加号可以连接字符串
print("hi" + " tom")

# Python不支持字符类型，单字符在Python中也是作为一个字符串使用
str3 = "A"
print(f"str3的类型是：{type(str3)}")    # <class 'str'>

# 用三个单引号'''内容'''，或者三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的，比如输出一段代码
print("""
    既不回头，何必不忘。既然无缘，何需誓言。
    今日种种，似水无痕。明日何夕，君已陌路。
    """)
# 在字符串前面加’r‘可以使整个字符串不会被转义
str4 = "jack\ntom\tking"
print(str4)
str5 = r"jack\ntom\tking"
print(str5)

# 字符串的驻留机制
str1 = "Hello"
str2 = "Hello"
str3 = "Hello"
# 输出字符串的地址
# id()函数可以返回对象/数据的内存地址
print("str1的地址是：", id(str1))   # 1877534532800
print("str2的地址是：", id(str2))   # 1877534532800
print("str3的地址是：", id(str3))   # 1877534532800

str1 = "abc123#"
str2 = "abc123#"
id(str1)
id(str2)
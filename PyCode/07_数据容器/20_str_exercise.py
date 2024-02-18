"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/18 23:22
@File    :   20_str_exercise.py
@Author  :   Saber 
------------------------------------
"""

'''
定义一个字符串,str_names = "tom jack mary nuonuo smith saber"
    1) 统计一共有多少个人名
    2) 如果有"saber"则替换成"阿尔托莉雅"
    3) 如果人名是英文,则把首字母改成大写
'''
str_names = "tom jack mary nuonuo smith saber"
# 统计一共有多少个人名
str_names_split = str_names.split(" ")
print(f"一共有{len(str_names_split)}个人名")
print(str_names_split)
# 如果有"saber"则替换成"阿尔托莉雅"
str_names_new = str_names.replace("saber", "阿尔托莉雅")
print(str_names_new)
# 如果人名是英文,则把首字母改成大写
'''
思路分析：
['tom', 'jack', 'mary', 'nuonuo', 'smith', 'saber'] -> ['Tom', 'Jack', 'Mary', 'Nuonuo', 'Smith', 'Saber']
    1) 定义一个新的字符串str_names_upper来保存结果
    2) 遍历str_names_split列表,如果是英文名 => 首字母大写,如果不是英文名 => 则不发生变化,直接拼接到字符串后面
    3) str.capitalize():返回原字符串的副本,其首个字符大写,其余为小写
    4) 拼接到str_names_upper
'''
# 先将字符串转换为列表list
str_names_upper = ""
str_names_split = str_names_new.split(" ")
# 主要操作
# 是英文名 => 首字母大写
# 不是英文名 => 直接拼接到新的字符串后面
for ele in str_names_split:
    if ele.encode('utf-8').isalpha():
        str_names_upper += ele.replace(ele, ele.capitalize()) + "|"
    else:
        str_names_upper += ele

# 去掉两边的"|"
str_names_upper = str_names_upper.replace(str_names_upper, str_names_upper.strip("|"))
print(str_names_upper)
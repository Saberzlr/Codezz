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
# 如果有"saber"则替换成"阿尔托莉雅"
str_names_new = str_names.replace("saber", "阿尔托莉雅")
print(str_names_new)
# 如果人名是英文,则把首字母改成大写
print(str_names_new.upper())
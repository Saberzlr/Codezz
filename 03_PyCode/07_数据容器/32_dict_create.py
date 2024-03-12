"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/22 00:32
@File    :   32_dict_create.py
@Author  :   Saber 
------------------------------------
"""

# zip()可以将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，返回由这些元组组成的列表
books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹" ,"罗贯中", "吴承恩", "施耐庵"]
print({book:author for book,author in zip(books, authors)})

# 思考题
str1 = "Saber"
print({ele1:ele2 * 2 for ele1, ele2 in zip(str1, str1)})


# 案例
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
# 要求生成一个字典{'红色':'RED', '黑色':'BLACK', '黄色':YELLOW', '白色':'WHITE'}
# 方法1
e_l = list()
for ele in english_list:
    ele = ele.upper()
    e_l.append(ele)
print({ele1:ele2 for ele1, ele2 in zip(chinese_list, e_l)})
# 方法2
print({ele1:ele2.upper() for ele1, ele2 in zip(chinese_list, english_list)})
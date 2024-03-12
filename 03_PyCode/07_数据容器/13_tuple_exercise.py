"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/17 23:32
@File    :   13_tuple_exercise.py
@Author  :   Saber 
------------------------------------
"""

'''
定义一个元组,('大话西游', '周星驰', 80, ['周星驰', '小甜甜']),信息为(片名, 导演, 票价, 演员列表)
1) 查询票价对应索引
2) 遍历所有所有的演员
3) 删除'小甜甜'
4) 增加演员'牛魔王'、'猪八戒'
'''
tuple_movie = ('大话西游', '周星驰', 80, ['周星驰', '小甜甜'])
# 1) 查询票价对应索引
print(f"票价对应的索引为:{tuple_movie.index(80)}")

# 2) 遍历所有所有的演员
for ele in tuple_movie[-1]:
    print(ele)

# 3) 删除'小甜甜'
del tuple_movie[-1][1]
print(tuple_movie[-1])

# 4) 增加演员'牛魔王'、'猪八戒'
list = ['牛魔王', '猪八戒']
tuple_movie[-1].extend(list)
print(tuple_movie[-1])
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 17:33
@File    :   28_set_exercise.py
@Author  :   Saber 
------------------------------------
"""

'''
用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '二狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}
1) 求选课学生总共有多少人
2) 求只选了第一个学科(history)的学生数量和学生名字
3) 求只选了一门学科的学生数量和学生名字
4) 求选了三门学科的学生数量和学生名字
'''
s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '二狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}

# 求选课学生总共有多少人
# fun1
s_union = s_history.union(s_politic, s_english)
# fun2
s_union = s_history | s_politic | s_english
print(f"选课学生总共有:{len(s_union)}人")

print("-" * 40)

# 求只选了第一个学科(history)的学生数量和学生名字
# fun1
s_new01 = s_history.difference(s_english, s_politic)
# fun2
s_new01 = s_history - s_english - s_politic
print(f"只选了history学科的学生为:{len(s_new01)}人,学生名单为:")
for ele in s_new01:
    print(ele)

print("-" * 40)

# 求只选了一门学科的学生数量和学生名字
'''
思路分析:
	1) 求出只选择了history的学生
	2) 求出只选择了politic的学生
	3) 求出只选择了english的学生
	4) 最后对三个结果求并集
'''
# fun1
s_new02 = s_history.difference(s_english, s_politic).union(s_english.difference(s_history, s_politic), s_politic.difference(s_history, s_english))
# fun2
s_new02 = s_history - s_english - s_politic | s_english - s_history - s_politic | s_politic - s_english - s_history
print(f"只选了一门学科的学生数量为:{len(s_new02)}人,学生名单为:")
for ele in s_new02:
    print(ele)

print("-" * 40)

# 求选了三门学科的学生数量和学生名字
# fun1
s_new03 = s_history.intersection(s_politic, s_english)
# fun2
s_new03 = s_history & s_english & s_politic
print(f"选了三门学科的学生数量为:{len(s_new03)}人,学生名字为:{s_new03}")
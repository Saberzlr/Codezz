"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/19 16:33
@File    :   26_set_operations.py
@Author  :   Saber 
------------------------------------
"""

# 集合常用操作
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# 求集合元素的个数
print("basket的元素个数为:", len(basket))

# 判断apple是否在集合中
print("apple是否在集合中:", "apple" in basket)

# 将grape添加到集合中
basket.add('grape')
print("basket:", basket)

# 将apple从集合中删除
basket.remove('apple')
print("basket:", basket)

# 从集合中随机删除一个元素
ele = basket.pop()
print("ele:", ele, " 类型是:", type(ele))
# pop()操作会影响到原集合
print("basket:", basket)

# union():返回一个新集合
books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}
# 将books和books_2进行合集操作[求出在books集合或者在books_2集合的元素]
books_3 = books.union(books_2)
# 与上面的等价
books_3 = books | books_2
print("books_3:", books_3)

# intersection(*others):返回一个新集合
# 其中包含原集合以及others指定的所有集合中共有的元素
# 对books和books_2求交集[求出既在books又在books_2集合的元素]
books_4 = books.intersection(books_2)
# 与上面的等价
books_4 = books & books_2
print("books_4:", books_4)

# 求出只存在books集合中的元素
books_5 = books - books_2
# 与上面的等价
books_5 = books.difference(books_2)
print("books_5:", books_5)

# 求出只存在books2集合中的元素
books_6 = books_2 - books
# 与上面的等价
books_6 = books_2.difference(books)
print("books_6:", books_6)
"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/25 20:40
@File    :   02_seq_search.py
@Author  :   Saber 
------------------------------------
"""

name_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王"]
name = input("请输入你猜的名称:")
'''
# 法一
find_index = name_list.index(name)
print("index =", find_index)
'''
# 法二
find_index = -1
def seq_search(list, find_val):
    """_summary_
    顺序查找指定的元素
    Args:
        list (_type_): 传入要查找的列表 
        find_val (_type_): 传入要查找的元素
        return: 返回find_index
    """
    for i in range(len(name_list)):
        if find_val == name_list[i]:
            print(f"找到了:){find_val},其对应的下标为{i}")
            find_index = i
            break
    else:
        print(f"没有找到{find_val}:(")
    return find_index
seq_search(name_list, name)


# 如果一个列表中有多个要查找的元素/值，怎样才能把满足查询条件的元素的下表都返回。
'''
思路分析：
1. 顺序查找函数,把满足查询条件的元素的下标都返回
2. 用列表保存查找到的索引下标,发现一个就动态的添加到列表
3. 最终返回一个列表
    1) 遍历列表,列表为空 => 没找到
    2) 列表不为空 => 遍历输出
'''
name_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王", "青翼蝠王", "紫衫龙王"]
name = input("请输入你猜的名称:")

# 定义一个空列表
new_list = []

def seq_searcH(list, find_val):
    """_summary_
    顺序查找指定的元素
    Args:
        list (_type_): 传入要查找的列表 
        find_val (_type_): 传入要查找的元素
        return: 返回new_list
    """
    for i in range(len(name_list)):
        if find_val == name_list[i]:
            new_list.append(i)
    return new_list

seq_searcH(name_list, name)
if len(new_list):
    for ele in new_list:
        print(f"找到了:){name_list[ele]} 下标为:{ele}")
else:
    print("没找到:(")
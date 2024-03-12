"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/22 00:56
@File    :   33_dict_exercise.py
@Author  :   Saber 
------------------------------------
"""

clerks = {
    "0001": {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "sal": 12000
    },
    "0002": {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "sal": 10000
    },
    "0010": {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "sal": 20000
    }
}


# 通过员工号(0010),可以查询到员工的信息
print(f"0010号员工的信息为: 名字:{clerks["0010"]["name"]}-年龄{clerks["0010"]["age"]}-入职时间:{clerks["0010"]["entry_time"]}-薪水:{clerks["0010"]["sal"]}")


print("-" * 34)
# 根据需要,可以动态的增加、删除员工
# 增加:(员工号:0020, 年龄:30, 名字:Saber, 入职时间:2020-08-04, 薪水:6000)
# 删除:0001号员工
clerks["0020"] = {"age": 30, "name": "Saber", "entry_time": "2020-08-04", "sal": 6000}
print(f"clerks:{clerks}")
del clerks["0001"]
print(f"clerks:{clerks}")


print("-" * 34)
# 根据需要,可以修改员工的信息
# 修改:员工号为0020的,名字:'阿尔托莉雅',入职时间:2002-04-01,薪水在原来的基础上增加10%
clerks["0020"]["name"] = {"阿尔托莉雅"}
clerks["0020"]["entry_time"] = {"2002-04-01"}
# clerks["0020"]["sal"] = {round(6000 * (1 + 0.1), 1)}
clerks["0020"]["sal"] += clerks["0020"]["sal"] * 0.1
print(f"clerks:{clerks}")


print("-" * 34)
# 遍历 所有员工,把所有员工的薪水,在原工资的基础上,增加20%
# 员工号为
# 法1
for ele1 in clerks:
    print(f"员工号为{ele1}的信息如下:")
    print(f"年龄:{clerks[ele1]["age"]}-名字:{clerks[ele1]["name"]}-入职时间:{clerks[ele1]["entry_time"]}-薪水:{round(clerks[ele1]["sal"] * (1 + 0.1), 1)}")
# 法2
print("-" * 34)
keys = clerks.keys()
for key in keys:
    clerk_info = clerks[key]
    print(f"员工号为{key}的信息如下:")
    print(f"年龄:{clerk_info["age"]}-名字:{clerk_info["name"]}-入职时间:{clerk_info["entry_time"]}-薪水:{round(clerk_info["sal"] * (1 + 0.1), 1)}")
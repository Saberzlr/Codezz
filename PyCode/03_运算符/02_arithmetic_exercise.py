"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/03 22:48
@File    :   02_arithmetic_exercise.py
@Author  :   Saber 
------------------------------------
"""

# 假如还有97天放假，问：合xx个星期零xx天
'''
    思路分析：
    1. 定义变量
    day_total: 记录总天数
    weeks: 记录几个星期
    days: 记录剩余几天
    2. weeks: day_total // 7
    3. days: days % 7
    4. 输出信息
'''
day_total = 97
# weeks = int(day_total / 7)
weeks = day_total // 7
days = day_total % 7
# print(f"合{int(day_total / 7)}个星期零{day_total % 7}天")
print("合" + str(weeks) + "个星期零" + str(days) + "天")

'''
    思路分析：
    1. 定义变量
    fh: 华氏温度
    cd: 摄氏温度
    2. 公式: cd = 5 / 9 *(fh - 100)
    3. 输出信息
'''
# 定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：5/9*(华氏温度-100)，请求出华氏温度对应的摄氏温度。[234.5]
fh = 234.5
cd = 5 / 9 * (fh - 100)
print("华氏温度:%.2f 对应的摄氏温度:%.2f" %(fh, cd))
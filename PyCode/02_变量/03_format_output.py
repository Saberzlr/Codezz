# @Version : 1.0
# @Author  : zy
# @File    : 03_format_output.py
# @Time    : 2024/2/1 17:55

# 格式化输出

# 定义变量
age = 50
score = 90.5
gender = '男'
name = "李逍遥"

# %操作符格式化输出
print("个人信息：%s-%d-%s-%.2f" % (name, age, gender, score))

# format()函数
# 占位符可以少，但是不能多
print("个人信息：{}-{}-{}-{}".format(name, age, gender, score))

# f-strings
print(f"个人信息：{name}-{age}-{gender}-{score}")
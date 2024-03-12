"""
------------------------------------
@Version :   1.0
@Time    :   2024/02/06 18:03
@File    :   22_mutiply_for_exercise02.py
@Author  :   Saber 
------------------------------------
"""

# 打印空心菱形
'''
    *              *
   * *            * *
  *   *     =>   *   *
 *     *        *     *
*********      *       *
                *     *
                 *   *
                  * *
                   *
思路分析:5
    1. 在打印出空心金字塔的情况下,可以分为上下两部分打印
        1) 上半部分:打印出空心金字塔,上半部分最后一行不将"*"全部输出,而是遵循上述的规则,只有第一个和最后一个输出"*",其余位置输出" "(空格)
        2) 下半部分:
    2. 下半部分打印倒三角
*****        ****          *******          *     *
*****   =>   ***     =>     *****     =>     *   *
*****        **              ***              * *
*****        *                *                *
    3. 其余思路同打印空心金字塔:
    第一层:4个*  7个*   1个空格
    第二层:3个*  5个*   2个空格
    第三层:2个*  3个*   3个空格
    第四层:1个*  1个*   4个空格
'''

total_level = int(input("请输入你要打印的层数(奇数):"))
# 打印上半部分
for i in range(1, (total_level // 2 + 1) + 1):
    for k in range((total_level // 2 + 1) - i):
        print(" ", end = "")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 1 - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print("\n")

# 打印下半部分
for i in range(1, (total_level // 2 + 1)):
    for k in range(1, i + 1):
        print(" ", end = "")
    for j in range(1, 2 * ((total_level // 2 + 1) - i)):
        if j == 1 or j == 2 * ((total_level // 2 + 1) - i) - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print("\n")
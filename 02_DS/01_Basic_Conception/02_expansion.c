/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/08 17:20
 * @file    :   02_expansion.c
 * @author  :   Saber
 * @brief   :   clock()函数的拓展
 * ***********************************
 */

/*----------------测试函数执行时间的模板----------------*/

// clock()函数：捕捉从程序开始运行到clock()被调用时所耗费的时间。这个时间单位是clock tick，即：“时钟打点”。
// 常数CLK_TCK：机器时钟每秒所走的时钟打点数。
#include <stdio.h>
#include <time.h>

// clock_t是clock()函数 返回的变量类型
clock_t start, stop;
// 记录被测函数的运行时间，以秒为单位
double duration;
int main()
{
    // 不在测试范围内的准备工作写在clock()调用之前
    start = clock(); // 开始计时
    // MyFunction();    // 把被测函数写在此处
    stop = clock(); // 停止计时
    duration = ((double)(stop - start)) / CLK_TCK;
    // 计算运行时间
    // 其他不在测试范围的处理写在后面，例如：输出duration的值

    return 0;
}
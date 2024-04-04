/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/04 16:39
 * @file    :   02_expansion_template.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

/*----------------测试函数执行时间的模板----------------*/

// clock()函数：捕捉从程序开始运行到clock()被调用时所耗费的时间。这个时间单位是clock tick，即：“时钟打点”。
// 常数CLK_TCK：机器时钟每秒所走的时钟打点数。[不同的机器不同]
// 配合使用，可以算出程序执行花费了多长时间[以秒为单位]
#include <stdio.h>
#include <time.h>

// clock_t是clock()函数 返回的变量类型
clock_t start, stop;
// 记录被测函数的运行时间[以秒为单位]
double duration;
// 被测函数最大重复调用次数
#define MAX_K 1e7

int main()
{
    // 不在测试范围内的准备工作写在clock()调用之前
    start = clock(); // 开始计时
    // 让被测函数重复执行充分多次，使得测出的总的时钟打点间隔充分长，最后计算被测函数平均每次运行的时间即可。
    // MyFunction();    // 把被测函数写在此处
    stop = clock(); // 停止计时
    duration = ((double)(stop - start)) / CLK_TCK;
    // 计算运行时间
    // 其他不在测试范围的处理写在后面，例如：输出duration的
    printf("%ticks = %f\n", ((double)(stop - start)) / CLK_TCK);
    printf("duration = %6.2e\n", duration / MAX_K);

    return 0;
}
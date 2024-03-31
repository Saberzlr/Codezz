/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 18:26
 * @file    :   7_6.c
 * @author  :   Saber
 * @brief   :   厘米换算英尺英寸
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    double cm;
    int foot, inch;
    scanf("%lf", &cm);

    // 单位转换
    foot = cm / 100 / 0.3048;
    inch = ((cm / 100 / 0.3048) - foot) * 12;

    // 输出
    printf("%d %d", foot, inch);

    return 0;
}
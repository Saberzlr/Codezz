/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 19:59
 * @file    :   7_7.c
 * @author  :   Saber
 * @brief   :   计算摄氏温度
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    double C, F;
    scanf("%lf", &F);

    // 温度转换
    C = 5 * (F - 32) / 9;
    printf("Celsius = %d", (int)C);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 18:23
 * @file    :   7_56.c
 * @author  :   Saber
 * @brief   :   求给定精度的简单交错序列部分和
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
int main()
{
    // 分子: 1 1 1 1 ...
    // 分母: 1 4 7 10...
    // 输入
    double eps;
    scanf("%lf", &eps);

    // 求和
    double sum = 0;
    int flag = 1;
    int i = 1;
    while (1)
    {
        sum += 1.0 / i * flag;
        flag = -flag;
        if (eps >= 1.0 / i)
        {
            break;
        }
        i += 3;
    }

    // 输出
    printf("sum = %.6f", sum);

    return 0;
}
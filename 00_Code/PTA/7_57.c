/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 20:02
 * @file    :   7_57.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <stdio.h>

double fact(int n)
{
    double fac = 1;
    if (n > 0)
    {
        for (int i = 1; i <= n; i++)
        {
            fac *= i * 1.0;
        }
    }
    return fac;
}

int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 求和
    double sum = 0;
    for (int i = 0; i <= n; i++)
    {
        sum += 1.0 / fact(i);
    }

    // 输出
    printf("%.8f", sum);

    return 0;
}
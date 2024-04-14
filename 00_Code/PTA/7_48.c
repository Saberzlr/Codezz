/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 11:34
 * @file    :   7_48.c
 * @author  :   Saber
 * @brief   :   求组合数
 * ***********************************
 */

#include <stdio.h>

double fact(int n)
{
    double fac = 1;
    for (int i = 1; i <= n; i++)
    {
        fac *= i;
    }
    return fac;
}

int main()
{
    // 输入
    int m, n;
    scanf("%d %d", &m, &n);

    // 计算Cnm
    double res;
    res = fact(n) / (fact(m) * fact(n - m));

    // 输出
    printf("result = %.0f", res);

    return 0;
}
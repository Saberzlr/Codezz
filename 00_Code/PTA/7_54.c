/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 17:58
 * @file    :   7_54.c
 * @author  :   Saber
 * @brief   :   求阶乘序列前N项和
 * ***********************************
 */

#include <stdio.h>

// 求阶乘
int fact(int n)
{
    int fac = 1;
    for (int i = 1; i <= n; i++)
    {
        fac *= i;
    }
    return fac;
}

int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 求阶乘和
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += fact(i);
    }

    // 输出
    printf("%d", sum);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 23:33
 * @file    :   7_41.c
 * @author  :   Saber
 * @brief   :   计算阶乘和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);
    int sum = 0;
    int fac;

    // 求阶乘和
    for (int i = 1; i <= n; i++)
    {
        fac = 1;
        for (int j = 1; j <= i; j++)
        {
            fac *= j;
        }
        sum += fac;
    }

    // 输出
    printf("%d", sum);

    return 0;
}
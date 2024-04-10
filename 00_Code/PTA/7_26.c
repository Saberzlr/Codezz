/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/08 00:23
 * @file    :   7_26.c
 * @author  :   Saber
 * @brief   :   最大公约数和最小公倍数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int m, n, min, max;
    scanf("%d %d", &m, &n);
    int gys;
    int gbs;

    // 求最大公约数
    // 求出m和n中较小的
    if (m > n)
    {
        min = n;
        max = m;
    }
    else
    {
        min = m;
        max = n;
    }
    for (int i = min; i > 0; i--)
    {
        if (max % i == 0)
        {
            gys = i;
            break;
        }
    }

    // 求最小公倍数
    gbs = (m / gys) * (n / gys) * gys;
    // 输出
    printf("%d %d", gys, gbs);

    return 0;
}
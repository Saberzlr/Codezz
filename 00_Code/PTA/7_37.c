/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 11:43
 * @file    :   7_37.c
 * @author  :   Saber
 * @brief   :   输出整数各位数字
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 分解数字
    // 1. 统计位数
    int mask = 1;
    int t = n;
    while (t > 9)
    {
        t /= 10;
        mask *= 10;
    }
    // 2. 分解数字
    int a;
    while (mask)
    {
        a = n / mask;
        n %= mask;
        mask /= 10;
        printf("%d ", a);
    }

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 19:00
 * @file    :   7_30.c
 * @author  :   Saber
 * @brief   :   念数字
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    char ch;
    scanf("%d", &n);

    // 相关的OP
    // 先正向分解数字
    // 0. 分正数 / 负数
    if (n < 0)
    {
        n = -n;
        printf("fu ");
    }
    int temp = n;
    // 1. 求位数
    int count = 1;
    int mask = 1;
    while (temp > 9)
    {
        mask *= 10;
        count++;
        temp /= 10;
    }
    // printf("%d %d", count, mask);
    // 2. 分解数字
    int x = 1;
    int m;
    x *= mask;
    do
    {
        m = n / mask;
        n -= mask * m;
        mask /= 10;
        // printf("%d %d %d\n", m, temp, mask);

        // 再用switch-case语句
        switch (m)
        {
        case 0:
            printf("ling");
            break;
        case 1:
            printf("yi");
            break;
        case 2:
            printf("er");
            break;
        case 3:
            printf("san");
            break;
        case 4:
            printf("si");
            break;
        case 5:
            printf("wu");
            break;
        case 6:
            printf("liu");
            break;
        case 7:
            printf("qi");
            break;
        case 8:
            printf("ba");
            break;
        case 9:
            printf("jiu");
            break;
        default:
            break;
        }
        if (mask)
        {
            printf(" ");
        }
    } while (mask > 0);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 20:47
 * @file    :   08.c
 * @author  :   Saber
 * @brief   :   念整数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int num;
    int mask = 1;
    int cnt1 = 1, cnt2 = 0;
    scanf("%d", &num);
    int t = num;
    // 对于负数要特殊处理 => 先取相反数变为正数，然后进行和正数一样的处理
    if (num < 0)
    {
        printf("fu ");
        num = -num;
        t = num;
    }
    // 先分解数字
    while (t > 9)
    {
        t /= 10;
        mask *= 10;
        cnt1++;
    }
    // 输出数字对应的拼音
    while (mask)
    {
        int d = num / mask;
        num %= mask;
        mask /= 10;
        // printf("%d ", d);
        switch (d)
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
        cnt2++;
        if (cnt2 < cnt1)
        {
            printf(" ");
        }
    }

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/25 19:11
 * @file    :   03.c
 * @author  :   Saber
 * @brief   :   时间换算
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int BJT, UTC;
    scanf("%d", &BJT);
    int hour = BJT / 100;
    int min = BJT % 100; //
    // printf("%d %d", hour, min);
    // 处理小时
    if (hour - 8 >= 0)
    {
        hour -= 8;
    }
    else
    {
        hour += 16;
    }
    // 输出
    UTC = hour * 100 + min;
    if (hour == 0)
    {
        printf("%d", min);
    }
    else
    {
        printf("%d%02d", hour, min);
    }

    return 0;
}
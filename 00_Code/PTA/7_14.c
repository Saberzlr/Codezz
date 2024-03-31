/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:37
 * @file    :   7_14.c
 * @author  :   Saber
 * @brief   :   然后是几点
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int time, gap;
    scanf("%d %d", &time, &gap);
    // 方法1
    // 1. 先分离 小时 和 分钟
    int hour, min;
    hour = time / 100;
    min = time % 100;
    // 2. 将时间转换成分钟制
    time = hour * 60 + min;
    // 3. 计算时间
    time += gap;
    // 4. 还原成要求输出的格式
    hour = time / 60;
    min = time % 60;
    /*
        // 方法2
        // 1. 先分离 小时 和 分钟
        int hour, min;
        hour = time / 100; // 11:20
        min = time % 100;

        int hour1, min1;
        hour1 = gap / 60; // 1:10
        min1 = gap % 60;
        // 2. 分情况讨论
        if (gap >= 0)
        {
            min += min1;
            if (min >= 60)
            {
                hour += 1;
                min -= 60;
            }
            hour += hour1;
            hour %= 24;
        }
        else
        {
            min += min1;
            if (min < 0)
            {
                hour -= 1;
                min += 60;
            }
            hour += hour1 + 24;
            hour %= 24;
        }
    */
    // 输出
    printf("%d%02d", hour, min);

    return 0;
}
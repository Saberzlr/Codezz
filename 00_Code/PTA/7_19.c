/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 22:43
 * @file    :   7_19.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

// 拓展常识：
// 一年一共有365天或者366天，平年有365天，闰年有366天，闰年每隔4年一次。
// 平年的2月是28天，闰年2月是29天。
// 4月、6月、9月、11月各是30天。
// 1月、3月、5月、7月、8月、10月、12月各是31天。
#include <stdio.h>
int main()
{
    // 输入
    int year, month, day;
    int total_day = 0;
    scanf("%d/%d/%d", &year, &month, &day);

    // 1. 判断是否是闰年
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))
    {
        for (int i = month - 1; i > 0; i--)
        {
            // 此处也可以用switch-case语句来实现
            if (i == 4 || i == 6 || i == 9 || i == 11)
            {
                total_day += 30;
            }
            else if (i == 2)
            {
                total_day += 29;
            }
            else
            {
                total_day += 31;
            }
        }
    }
    else
    {
        for (int i = month - 1; i > 0; i--)
        {
            if (i == 4 || i == 6 || i == 9 || i == 11)
            {
                total_day += 30;
            }
            else if (i == 2)
            {
                total_day += 28;
            }
            else
            {
                total_day += 31;
            }
        }
    }

    // 输出
    total_day += day;
    printf("%d", total_day);

    return 0;
}
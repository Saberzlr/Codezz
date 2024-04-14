/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 11:34
 * @file    :   7_50.c
 * @author  :   Saber
 * @brief   :   输出华氏-摄氏温度转换表
 * ***********************************
 */

#include <stdio.h>

int main()
{
    // 输入
    int lower, upper;
    scanf("%d %d", &lower, &upper);
    double cel;

    // 转换表及打印输出
    int i;
    if (lower <= upper && upper <= 100)
    {
        printf("fahr celsius\n");
        for (i = lower; i <= upper; i += 2)
        {
            cel = 5.0 * (i - 32) / 9;
            printf("%d%6.1f\n", i, cel);
        }
    }
    else
    {
        printf("Invalid.");
    }

    return 0;
}
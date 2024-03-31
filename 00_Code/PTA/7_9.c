/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:09
 * @file    :   7_9.c
 * @author  :   Saber
 * @brief   :   求整数均值
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int v1, v2, v3, v4;
    scanf("%d %d %d %d", &v1, &v2, &v3, &v4);

    // 计算
    int sum = 0;
    double avg;
    sum = v1 + v2 + v3 + v4;
    avg = sum / 4.0;

    // 输出
    printf("Sum = %d; Average = %.1f", sum, avg);

    return 0;
}
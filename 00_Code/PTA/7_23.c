/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/07 18:25
 * @file    :   7_23.c
 * @author  :   Saber
 * @brief   :   分段计算居民水费
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int x;
    double y;
    scanf("%d", &x);

    // 计算
    if (x <= 15)
    {
        y = 4.0 * x / 3;
    }
    else
    {
        y = 2.5 * x - 17.5;
    }

    // 输出
    printf("%.2f", y);

    return 0;
}
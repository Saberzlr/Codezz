/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:13
 * @file    :   7_10.c
 * @author  :   Saber
 * @brief   :   算术入门之加减乘除
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int a, b;
    scanf("%d %d", &a, &b);
    // 计算并输出
    printf("%d + %d = %d\n", a, b, a + b);
    printf("%d - %d = %d\n", a, b, a - b);
    printf("%d * %d = %d\n", a, b, a * b);
    if (a % b == 0)
    {
        printf("%d / %d = %d", a, b, a / b);
    }
    else
    {
        printf("%d / %d = %.2f", a, b, a * 1.0 / b);
    }

    return 0;
}
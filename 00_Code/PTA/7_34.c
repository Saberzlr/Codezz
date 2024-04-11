/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/11 11:51
 * @file    :   7_34.c
 * @author  :   Saber
 * @brief   :   求分数序列前N项和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 分子: 2 3 5 8
    // 分母: 1 2 3 5
    // 输入
    int n;
    scanf("%d", &n);
    double sum = 0;

    // 求和
    double a = 2; // 分子
    double b = 1; // 分母
    double t;
    while (n)
    {
        sum += a / b;
        t = a;
        a = a + b;
        b = t;
        // a = a + b;
        // b = a - b;
        n--;
    }

    // 输出
    printf("%.2f", sum);

    return 0;
}
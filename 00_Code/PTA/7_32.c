/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/11 12:20
 * @file    :   7_32.c
 * @author  :   Saber
 * @brief   :   求交错序列前N项和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 分子: 1 2 3 4 5 6
    // 分母: 1 3 5 7 9 11
    // 输入
    int n;
    scanf("%d", &n);
    double sum = 0.0;

    // 求和
    int flag = 1;
    int a = 1;
    int b = 1;
    while (n)
    {
        sum += (a * 1.0 / b) * flag;
        flag = -flag;
        a++;
        b += 2;
        n--;
    }

    // 输出
    printf("%.3f", sum);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 17:50
 * @file    :   7_52.c
 * @author  :   Saber
 * @brief   :   求简单交错序列前N项和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 分子: 1 1 1 1 ...
    // 分母: 1 4 7 10...
    // 输入
    int n;
    scanf("%d", &n);
    int flag = 1;

    // 求和
    double sum = 0;
    int i = 1;
    while (n)
    {
        sum += 1.0 / i * flag;
        flag = -flag;
        i += 3;
        n--;
    }

    // 输出
    printf("sum = %.3f", sum);

    return 0;
}
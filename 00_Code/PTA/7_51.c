/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 11:34
 * @file    :   7_51.c
 * @author  :   Saber
 * @brief   :   求奇数分之一序列前N项和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);
    double sum = 0;
    // 用来统计当前加到了第几项
    int count = 1;

    // 求和
    for (int i = 1; count <= n; i++)
    {
        if (i % 2 == 1)
        {
            sum += 1.0 / i;
            count++;
        }
    }

    // 输出
    printf("sum = %.6f", sum);

    return 0;
}
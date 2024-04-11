/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/11 12:00
 * @file    :   7_33.c
 * @author  :   Saber
 * @brief   :   统计素数并求和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int m, n;
    scanf("%d %d", &m, &n);

    // 判断素数
    // 求和
    int isPrime;
    int cnt = 0, sum = 0;
    for (int i = m; i <= n; i++)
    {
        for (int j = 2; j <= i; j++)
        {
            isPrime = 1;
            if (i % j == 0 && i != j)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime)
        {
            sum += i;
            cnt++;
        }
    }

    // 输出
    printf("%d %d", cnt, sum);

    return 0;
}
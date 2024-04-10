/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 18:52
 * @file    :   7_28.c
 * @author  :   Saber
 * @brief   :   求整数的位数及各位数字之和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int N, num;
    scanf("%d", &N);
    int count = 0;
    int sum = 0;

    // 求位数 + 求各位数的和
    while (N)
    {
        num = N % 10;
        N /= 10;
        count++;
        sum += num;
    }

    // 输出
    printf("%d %d", count, sum);

    return 0;
}
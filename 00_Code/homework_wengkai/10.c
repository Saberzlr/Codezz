/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/21 15:52
 * @file    :   10.c
 * @author  :   Saber
 * @brief   :   多项式加法
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
int main()
{
    int a, b;           // a为输入的次幂，b为系数
    int sum[105] = {0}; // 存储不同次幂的系数
    int max = 0;        // 记录最大次幂
    for (int i = 0; i < 2; i++)
    { // 两个多项式
        do
        {
            scanf("%d %d", &a, &b);
            sum[a] += b;
            if (a > max)
            { // 寻求最高次幂
                max = a;
            }
        } while (a != 0);
    }
    int count = 0; // 记录符合条件的sum[i]
    for (int j = max; j >= 0; j--)
    {
        if (sum[j] != 0)
        {
            count++;
            if (sum[j] > 0)
            {
                if (count != 1)
                { // 首个数输出，特殊处理
                    printf("+");
                }
            }
            else
            {
                printf("-");
            }
            int k = abs(sum[j]); // 下面就是一大堆逻辑关系
            if (abs(sum[j]) == 1)
            {
                if (j == 1)
                {
                    printf("x");
                }
                else if (j == 0)
                {
                    printf("%d", k);
                }
                else
                {
                    printf("x%d", j);
                }
            }
            else
            {
                if (j == 1)
                {
                    printf("%dx", k);
                }
                else if (j == 0)
                {
                    printf("%d", k);
                }
                else
                {
                    printf("%dx%d", k, j);
                }
            }
        }
    }
    if (count == 0)
    { // 结果为0时的特殊处理
        printf("%d", 0);
    }
    printf("\n");
    return 0;
}
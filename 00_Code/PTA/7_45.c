/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/13 17:34
 * @file    :   7_45.c
 * @author  :   Saber
 * @brief   :   找完数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int m, n;
    scanf("%d %d", &m, &n);

    // 找完数
    int i, j;
    int sum;
    int isWan = 0;
    for (i = m; i <= n; i++)
    {
        sum = 0;
        for (j = 1; j < i; j++)
        {
            if (i % j == 0)
            {
                sum += j;
            }
        }
        if (sum == i)
        {
            isWan = 1;
            printf("%d = 1", sum);
            for (int k = 2; k < i; k++)
            {
                if (i % k == 0)
                {
                    printf(" + %d", k);
                }
            }
            printf("\n");
        }
    }

    if (isWan == 0)
    {
        printf("None");
    }

    return 0;
}
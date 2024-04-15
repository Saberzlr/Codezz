/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/15 10:43
 * @file    :   7_59.c
 * @author  :   Saber
 * @brief   :   打印菱形图案
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);
    /*
    // 1. 打印正方形
    // *****
    // *****
    // *****
    // *****
    // *****
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    // 2. 打印上三角
    // *
    // **
    // ***
    // ****
    // *****
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    // 3. 打印正三角
    //     *        4空格1*     第1行
    //    ***       3空格3*     第2行
    //   *****      2空格5*     第3行
    //  *******     1空格7*     第4行
    // *********    0空格9*     第5行
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 2 * 5; j++)
        {
            if (j - i < 5 && i + j >= 4)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    */
    // 打印

    // 上半部分
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 2 * n; j++)
        {
            if (j - i < n && i + j >= n - 1)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    // 下半部分
    for (int i = n; i < 2 * n - 1; i++)
    {
        for (int j = 0; j < 2 * n - 1; j++)
        {
            if (i - j < n && i + j <= 3 * (n - 1))
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 18:33
 * @file    :   test.c
 * @author  :   Saber
 * @brief   :   测试
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int a[][3] = {{0}, {1}, {3}};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", a[i][j]);
        }
    }

    return 0;
}
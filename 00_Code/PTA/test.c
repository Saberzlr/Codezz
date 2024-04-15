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
    for (int i = 5; i < 9; i++)
    {
        for (int j = 4; j > 9 - i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
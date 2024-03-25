/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/25 19:21
 * @file    :   04.c
 * @author  :   Saber
 * @brief   :   分队列
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int num;
    scanf("%d", &num);
    for (int i = 1; i <= num; i += 1)
    {
        if (i % 2)
        {
            printf("%d", i);
        }
        else if (i != num)
        {
            printf(" ");
        }
    }

    return 0;
}
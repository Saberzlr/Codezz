/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/12 15:40
 * @file    :   00_test.c
 * @author  :   Saber
 * @brief   :   test
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int x;
    int count[10] = {0};

    scanf("%d", &x);

    while (x != -1)
    {
        scanf("%d", &x);
        if (x >= 0 && x <= 9)
        {
            count[x]++;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", count[i]);
    }

    return 0;
}
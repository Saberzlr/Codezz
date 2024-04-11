/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 16:56
 * @file    :   05_isPrime.c
 * @author  :   Saber
 * @brief   :   找素数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int x, i;
    int cnt = 0;
    for (x = 2; cnt < 50; x++)
    {
        int isPrime = 1;
        for (i = 2; i <= x; i++)
        {
            if (x % i == 0 && x != i)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime)
        {
            printf("%d\n", x);
            cnt++;
        }
    }

    return 0;
}
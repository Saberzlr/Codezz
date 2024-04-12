/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 16:23
 * @file    :   12_relay_break.c
 * @author  :   Saber
 * @brief   :   接力break
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int x;
    int one, two, five;
    int exit = 0;

    scanf("%d", &x);
    for (one = 1; one < x * 10; one++)
    {
        for (two = 1; two < x * 10 / 2; two++)
        {
            for (five = 1; five < x * 10 / 2; five++)
            {
                if (one + two * 2 + five * 5 == x * 10)
                {
                    printf("可以用%d个1角 + %d个2角 + %d个5角得到%d元\n", one, two, five, x);
                    exit = 1;
                    break;
                }
            }
            if (exit == 1)
                break;
        }
        if (exit == 1)
            break;
    }

    return 0;
}
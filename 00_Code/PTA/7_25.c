/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/08 00:04
 * @file    :   7_25.c
 * @author  :   Saber
 * @brief   :   求奇数和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int num;
    int sum = 0;
    do
    {
        scanf("%d", &num);
        if (num == 0 || num < 0)
        {
            continue;
        }
        else
        {
            if (num % 2)
            {
                sum += num;
            }
        }
    } while (num != 0 && num >= 0);

    printf("%d", sum);

    return 0;
}
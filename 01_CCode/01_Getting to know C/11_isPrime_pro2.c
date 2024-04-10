/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 23:09
 * @file    :   11_isPrime_pro2.c
 * @author  :   Saber
 * @brief   :   求素数的加强版1
 * ***********************************
 */

/**
 * @brief 构造素数表
 * 1. 令x为2。
 * 2. 将2x、3x、4x直至ax<n的数标记为非素数。
 * 3. 令x为下一个没有被标记为非素数的数，重复步骤2；直至所有的数均已尝试完毕。
 */

#include <stdio.h>
int main()
{
    const int maxNumber = 25;
    int isPrime[maxNumber];
    int i;
    int x;
    for (i = 0; i < maxNumber; i++)
    {
        isPrime[i] = 1;
    }
    for (x = 2; x < maxNumber; x++)
    {
        if (isPrime[x])
        {
            for (i = 2; i * x < maxNumber; i++)
            {
                isPrime[i * x] = 0;
            }
        }
    }
    for (i = 2; i < maxNumber; i++)
    {
        if (isPrime[i])
        {
            printf("%d\t", i);
        }
    }
    printf("\n");

    return 0;
}
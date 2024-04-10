/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 22:48
 * @file    :   10_isPrime_pro1.c
 * @author  :   Saber
 * @brief   :   求素数的加强版1
 * ***********************************
 */

#include <stdio.h>

const int NUM = 10;
int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes);

int main()
{
    int prime[NUM] = {2};
    int count = 1;
    // 从3开始测试素数
    int i = 3;
    // 让输出好看些
    {
        int i;
        printf("\t\t");
        for (i = 0; i < NUM; i++)
        {
            printf("%d\t", i);
        }
        printf("\n");
    }
    while (count < NUM)
    {
        if (isPrime(i, prime, count))
        {
            // 如果是素数，将这个数字i加入到prime数组中
            // 先存放到指针所指的位置，再将指针移动到下一个位置
            prime[count++] = i;
        }
        // 用来作调试
        {
            printf("i = %d\t cnt=%d\t", i, count);
            int i;
            for (i = 0; i < NUM; i++)
            {
                printf("%d\t", prime[i]);
            }
            printf("\n");
        }
        i++;
    }
    for (i = 0; i < NUM; i++)
    {
        printf("%d", prime[i]);
        if ((i + 1) % 5)
        {
            printf("\t");
        }
        else
        {
            printf("\n");
        }
    }

    return 0;
}

int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes)
{
    int ret = 1;
    int i;
    for (i = 0; i < numberOfKnownPrimes; i++)
    {
        if (x % knownPrimes[i] == 0)
        {
            ret = 0;
            break;
        }
    }
    return ret;
}
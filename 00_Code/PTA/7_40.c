/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 12:27
 * @file    :   7_40.c
 * @author  :   Saber
 * @brief   :   到底是不是太胖了
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    while (n--)
    {
        int h, w;
        scanf("%d %d", &h, &w);

        double std;
        std = (h - 100) * 0.9 * 2;
        double bias;
        bias = w - std;

        // 判断
        if (-std * 0.1 < bias && bias < std * 0.1)
        {
            printf("You are wan mei!\n");
        }
        else if (bias <= -std * 0.1)
        {
            printf("You are tai shou le!\n");
        }
        else if (bias >= std * 0.1)
        {
            printf("You are tai pang le!\n");
        }
    }

    return 0;
}
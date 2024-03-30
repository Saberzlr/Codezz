/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/30 13:18
 * @file    :   01.c
 * @author  :   Saber
 * @brief   :   求两个数的较大值
 * ***********************************
 */

#include <stdio.h>
int get_Max(int v1, int v2)
{
    if (v1 >= v2)
    {
        return v1;
    }
    else
    {
        return v2;
    }
}

int main()
{
    int num1, num2;
    num1 = 10;
    num2 = 20;
    int max = get_Max(num1, num2);
    printf("Max = %d", max);

    return 0;
}
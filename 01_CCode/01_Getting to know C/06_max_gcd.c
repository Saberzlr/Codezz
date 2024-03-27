/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 17:54
 * @file    :   06_max_gys.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int num1, num2, min, gcd;
    scanf("%d %d", &num1, &num2);
    // 比较两个数的大小
    if (num1 < num2)
    {
        min = num1;
    }
    else
    {
        min = num2;
    }

    // 求最大公约数
    // 方法1：暴力求解
    for (int i = 1; i <= min; i++)
    {
        if (num2 % i == 0 && num1 % i == 0)
        {
            gcd = i;
            // break;   求最小公约数则加个break就可以
        }
    }
    printf("%d和%d的最大公约数是%d\n", num1, num2, gcd);

    return 0;
}
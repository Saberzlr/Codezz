/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 17:54
 * @file    :   06_max_gcd.c
 * @author  :   Saber
 * @brief   :   求最大公约数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 方法1：暴力求解 => 效率低
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

    for (int i = 1; i <= min; i++)
    {
        if (num2 % i == 0 && num1 % i == 0)
        {
            gcd = i;
            // break;   求最小公约数则加个break就可以
        }
    }
    printf("%d和%d的最大公约数是%d\n", num1, num2, gcd);

    // 方法2：辗转相除法
    /**
     * @brief 思路分析
     * 1. 如果b=0，计算结束，a就是最大公约数
     * 2. 否则，计算a除以b的余数，让a等于b，而b等于那个余数
     * 3. 回到第一步
     */
    int a, b, temp;
    scanf("%d %d", &a, &b);
    while (b)
    {
        temp = a % b;
        a = b;
        b = temp;
    }
    printf("gdc=%d\n", a);

    return 0;
}
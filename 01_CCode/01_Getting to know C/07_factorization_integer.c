/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 18:30
 * @file    :   07_factorization_integer.c
 * @author  :   Saber
 * @brief   :   整数分解
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 方法1(有瑕疵) 700 => 逆序输出结果是7(正确的应该是007)
    /**
     * @brief 思路分析
     * 1. 先逆序输出12345 => 54321
     * 2. 然后分解54321
     * 3. 最后逆序输出1 2 3 4 5
     */
    int val, x, t = 0;
    int temp;
    scanf("%d", &val);
    while (val)
    {
        x = val % 10;
        t = 10 * t + x;
        val /= 10;
    }

    // 定义一个中间变量来保存逆序输出的54321
    temp = t;

    while (temp)
    {
        x = temp % 10;
        printf("%d", x);
        // 控制末尾空格的输出 => 最后一轮val必小于10，此时不要输出空格
        if (temp > 9)
        {
            printf(" ");
        }
        temp /= 10;
    }

    printf("\n");

    // 方法2 => 从最高位开始分解输出
    int y;
    scanf("%d", &y);

    // 定义z来保存y，因为统计几位数的时候会影响y的值
    int z = y;
    int mask = 1;
    // 统计几位数 => 确定mask的值
    while (z > 9)
    {
        z /= 10;
        mask *= 10;
    }
    // printf("%d", mask);

    // 分解整数
    while (mask)
    {
        int d = y / mask;
        y %= mask;
        printf("%d", d);
        if (mask > 9)
        {
            printf(" ");
        }
        mask /= 10;
        // printf("%d %d %d\n", y, mask, d);
    }

    return 0;
}
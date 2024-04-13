/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/13 11:27
 * @file    :   7_42.c
 * @author  :   Saber
 * @brief   :   整除光棍
 * ***********************************
 */

// 思路分析：[111111 / 13  = 8547]
// 1   / 13 = 0...1
// 11  / 13 = 0...11
// 111 / 13 = 8...7
// 71  / 13 = 5...6
// 61  / 13 = 4...9
// 91  / 13 = 7...0

#include <stdio.h>
int main()
{
    // 输入
    int x;
    scanf("%d", &x);

    // 计算
    int mask = 1;
    int div, res;
    int count = 0;

    // 处理不够除的情况
    while (mask < x)
    {
        div = mask % x;
        mask = div * 10 + 1;
        count++;
    }

    // 模拟除法
    do
    {
        res = mask / x;
        div = mask % x;
        mask = div * 10 + 1;
        printf("%d", res);
        count++;
    } while (div != 0);
    printf(" %d", count);

    return 0;
}
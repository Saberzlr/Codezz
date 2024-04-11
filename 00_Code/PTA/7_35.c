/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/11 11:39
 * @file    :   7_35.c
 * @author  :   Saber
 * @brief   :   猴子吃桃问题
 * ***********************************
 */

#include <stdio.h>

int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // OP
    // 第 N 天:       (1 + 1) * 2
    // 第 N - 1 天:   (4 + 1) * 2
    // 第 N - 2 天:   (10 + 1) * 2
    // ...
    // 第 1 天:       (f(2) + 1) * 2
    int res = 1;
    while (n != 1)
    {
        res = (res + 1) * 2;
        n--;
    }

    // 输出
    printf("%d", res);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:41
 * @file    :   7_16.c
 * @author  :   Saber
 * @brief   :   计算符号函数的值
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    int func;
    scanf("%d", &n);
    // 条件
    if (n < 0)
    {
        func = -1;
    }
    else if (n == 0)
    {
        func = 0;
    }
    else
    {
        func = 1;
    }
    // 输出
    printf("sign(%d) = %d", n, func);

    return 0;
}
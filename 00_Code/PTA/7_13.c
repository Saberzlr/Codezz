/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:29
 * @file    :   7_13.c
 * @author  :   Saber
 * @brief   :   后天
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int D;
    scanf("%d", &D);
    // 计算后天
    if (D <= 5)
    {
        D = D + 2;
    }
    else
    {
        D = D + 2 - 7;
    }
    // 输出
    printf("%d", D);

    return 0;
}
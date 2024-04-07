/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/07 18:18
 * @file    :   7_22.c
 * @author  :   Saber
 * @brief   :   用天平找小球
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int a, b, c;
    char differ;
    scanf("%d %d %d", &a, &b, &c);

    // 找不同
    if (a == b)
    {
        differ = 'C';
    }
    else
    {
        if (a == c)
        {
            differ = 'B';
        }
        else
        {
            differ = 'A';
        }
    }

    // 输出
    printf("%c", differ);

    return 0;
}
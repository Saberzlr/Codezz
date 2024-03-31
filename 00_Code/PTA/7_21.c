/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 22:05
 * @file    :   7_21.c
 * @author  :   Saber
 * @brief   :   超速判断
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int v;
    scanf("%d", &v);

    // 判断超速
    if (v > 60)
    {
        printf("Speed: %d - Speeding", v);
    }
    else
    {
        printf("Speed: %d - OK", v);
    }

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 11:20
 * @file    :   7_36.c
 * @author  :   Saber
 * @brief   :   韩信点兵
 * ***********************************
 */

#include <stdio.h>
const int n = 1e6;
int main()
{
    int i;
    for (i = 1; i < n; i++)
    {
        if ((i % 5 == 1) && (i % 6 == 5) && (i % 7 == 4) && (i % 11 == 10))
        {
            break;
        }
    }
    printf("%d", i);

    return 0;
}
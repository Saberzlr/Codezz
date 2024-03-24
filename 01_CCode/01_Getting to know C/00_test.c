/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/12 15:40
 * @file    :   00_test.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <stdio.h>
#include <string.h>

int sum (int x, int y)
{
    int z;
    z = x + y;
    return z;
}
int main()
{
    int a = 2, b = 4;
    int c = sum(a, b);
    int x = 5, y = 6;
    int cc = sum(x, y);
    printf("%d %d", c, cc);

    return 0;
}
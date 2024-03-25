/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/25 19:09
 * @file    :   02.c
 * @author  :   Saber
 * @brief   :   逆序的三位数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int num = 0;
    scanf("%d", &num);
    int n1 = num / 100;
    int n2 = num % 100 / 10;
    int n3 = num % 10;
    printf("%d", n3 * 100 + n2 * 10 + n1);

    return 0;
}
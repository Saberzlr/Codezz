/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/12 15:40
 * @file    :   00_test.c
 * @author  :   Saber
 * @brief   :   test
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int a = 10;
    int b = a++;                      // a++表示：先使用a的值，再将a+1
    printf("a = %d, b = %d\n", a, b); // a = 11, b = 10
    int c = ++a;                      // ++a表示：先将a+1，再使用a的值
    printf("a = %d, c = %d\n", a, c); // a = 12, c = 12

    return 0;
}
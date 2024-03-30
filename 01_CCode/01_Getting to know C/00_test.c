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
// 指针变量的大小取决于地址的大小
// 32位平台下地址是32个bit位（即4个字节）
// 64位平台下地址是64个bit位（即8个字节）
int main()
{
    printf("%d\n", sizeof(char *));   // 8
    printf("%d\n", sizeof(short *));  // 8
    printf("%d\n", sizeof(int *));    // 8
    printf("%d\n", sizeof(double *)); // 8

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 21:27
 * @file    :   7_15.c
 * @author  :   Saber
 * @brief   :   BCD解密
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int num;
    scanf("%d", &num);

    // 转换
    int ge, shi;
    shi = num / 16;
    ge = num % 16;

    // 输出
    printf("%d", shi * 10 + ge);

    return 0;
}
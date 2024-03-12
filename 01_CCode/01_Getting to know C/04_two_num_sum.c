/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/02/25 18:09
 * @file    :   04_two_num_sum.c
 * @author  :   Saber
 * @brief   :   计算两个数的和
 * ***********************************
 */

#include <stdio.h>

int main()
{
    // C语言语法规定：变量定义要放到当前代码块的最前面
    // 定义变量
    int num1 = 0, num2 = 0;
    int sum = 0;
    // 输入数据 - scanf函数
    scanf("%d %d", &num1, &num2); // & - 取地址符号
    sum = num1 + num2;

    printf("%d + %d = %d\n", num1, num2, sum);

    return 0;
}
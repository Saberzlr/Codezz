/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/02/25 17:29
 * @file    :   03_variable.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <stdio.h>
#include "03_sum.c"
/*
int num2 = 20;      // 全局变量 - 定义在大括号{}之外的变量
int main()
{
    int num1 = 10;  // 局部变量 - 定义在大括号{}内部的变量

    return 0;
} */
int global = 2019;
int main()
{
    int local = 2018;
    int global = 2020;
    printf("global = %d\n", global);
    {
        int a = 100;
    }
    // printf("%d\n", a);
    // 声明extern外部符号
    extern int g_val;
    printf("g_val = %d\n", g_val);

    return 0;
}
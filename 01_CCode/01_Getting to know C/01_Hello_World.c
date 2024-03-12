/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/02/25 15:33
 * @file    :   01_Hello_World.c
 * @author  :   Saber
 * @brief   :   初识C语言 - 打印Hello World!
 * ***********************************
 */

#include <stdio.h>

// main函数 - 主函数 => 程序的入口，且main函数有且仅有一个
// int是整型，main前面的int：main函数调用返回一个整型值
int main()
{
    // 在屏幕上输出"Hello World!"
    // 函数printf - print function - 打印函数
    // 将""内的东西原封不动的打印出来
    // 库函数 - C语言本身提供给程序员使用的函数 - 要使用库函数，必须先引用库函数 - #include <stdio.h>
    // stdio.h - standard input output - 标准输入输出
    printf("Hello World!\n");

    return 0; // 返回0
}
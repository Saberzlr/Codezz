/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/02/25 15:43
 * @file    :   02_Data_Types.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <stdio.h>

// %d - 打印整型
// %c - 打印字符
// %f - 打印浮点型
// %p - 以地址的形式打印
// %x - 打印十六进制
/*
int main()
{
    char ch = 'A';      // 向内存申请一片空间用来存放字符，这片空间的名字叫ch，ch里面存放一个字符'A'
    printf("%c\n", ch); // %c - 打印字符格式的数据

    int age = 20;
    printf("%d\n", age); // %d - 打印整型十进制数据

    short int num = 10;

    long val = 100;

    float score = 88.8;
    printf("%f\n", score);

    double score1 = 88.8;
    printf("%lf\n", score1);

    return 0;
} */
/*
int main()
{
    printf("%d\n", sizeof(char));       // 1
    printf("%d\n", sizeof(short));      // 2
    printf("%d\n", sizeof(int));        // 4
    printf("%d\n", sizeof(long));       // 4
    printf("%d\n", sizeof(long long));  // 8
    printf("%d\n", sizeof(float));      // 4
    printf("%d\n", sizeof(double));     // 8

    return 0;
} */
int main()
{
    short age = 20; // 向内存申请2个字节的空间，用来存放短整型20
    // 计算机中小数默认为double类型
    float score = 84.4f; // 向内存申请4个字节的空间，用来存放小数84.4

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:26
 * @file    :   7_12.c
 * @author  :   Saber
 * @brief   :   日期格式化
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int year, month, day;
    scanf("%d-%d-%d", &month, &day, &year);
    // 输出
    printf("%d-%02d-%02d", year, month, day);

    return 0;
}
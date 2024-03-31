/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:45
 * @file    :   7_17.c
 * @author  :   Saber
 * @brief   :   成绩转换
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int score;
    scanf("%d", &score);
    // 成绩转换 并 输出
    score /= 10;
    switch (score)
    {
    case 10:
    case 9:
        printf("A");
        break;
    case 8:
        printf("B");
        break;
    case 7:
        printf("C");
        break;
    case 6:
        printf("D");
        break;
    default:
        printf("E");
        break;
    }

    return 0;
}
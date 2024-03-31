/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:06
 * @file    :   7_8.c
 * @author  :   Saber
 * @brief   :   是不是太胖了
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int H;
    double W;
    scanf("%d", &H);

    // 计算标准体重
    W = (H - 100) * 0.9 * 2;

    // 输出体重
    printf("%.1f", W);

    return 0;
}
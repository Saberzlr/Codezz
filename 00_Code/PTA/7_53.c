/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 17:51
 * @file    :   7_53.c
 * @author  :   Saber
 * @brief   :   生成3的乘方表
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 乘方表
    int res;
    for (int i = 0; i <= n; i++)
    {
        res = pow(3, i);
        printf("pow(3,%d) = %d\n", i, res);
    }

    return 0;
}
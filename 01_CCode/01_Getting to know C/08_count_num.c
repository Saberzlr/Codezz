/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/02 12:17
 * @file    :   08_count_num.c
 * @author  :   Saber
 * @brief   :   统计每个数字[0 - 9]出现的次数
 * ***********************************
 */

#include <stdio.h>

const int num = 10;
int main()
{
    int x;
    int count[num];

    // 初始化
    for (int i = 0; i < num; i++)
    {
        count[i] = 0;
    }

    // 输入
    scanf("%d", &x);

    // 统计次数
    while (x != -1)
    {
        if (x >= 0 && x <= 9)
        {
            count[x]++;
        }
        scanf("%d", &x);
    }

    // 输出
    for (int i = 0; i < num; i++)
    {
        printf("%d:%d\n", i, count[i]);
    }

    return 0;
}
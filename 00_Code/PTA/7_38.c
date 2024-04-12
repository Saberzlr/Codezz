/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 15:44
 * @file    :   7_38.c
 * @author  :   Saber
 * @brief   :   支票面额
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    scanf("%d", &n);
    int getRes = 0;

    // 计算支票面额
    int i, j;
    for (i = 0; i < 100; i++)
    {
        for (j = 0; j < 100; j++)
        {
            if ((j * 100 + i) - n == i * 200 + 2 * j)
            {
                getRes = 1;
                printf("%d.%d\n", i, j);
            }
        }
    }
    if (getRes == 0)
    {
        printf("No Solution");
    }

    return 0;
}
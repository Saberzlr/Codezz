/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/21 16:05
 * @file    :   11.c
 * @author  :   Saber
 * @brief   :   找鞍点
 * ***********************************
 */

#include <stdio.h>

int main()
{
    int n, answer = 0; // answer用于判定是否有鞍点
    scanf("%d", &n);
    int num[n][n];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            scanf("%d", &num[i][j]);
        }
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            int flag1 = 1; // flag1判定此时的num[i][j]是否为第i行的最大值
            for (int t = 0; t < n; t++)
            {
                if (num[i][t] > num[i][j])
                {
                    flag1 = 0; // 遍历i行数据，若存在num[i][t]>num[i][j]，则判定flag1不通过
                    break;
                }
            }
            if (flag1)
            {                  // num[i][j]为第第i行的最大值时进入判定
                int flag2 = 1; // flag2判定此时的num[i][j]是否为第j列的最小值
                for (int t = 0; t < n; ++t)
                {
                    if (num[t][j] < num[i][j])
                    {
                        flag2 = 0; // 遍历j列数据，若存在num[t][j]<num[i][j]，则判定flag2不通过
                        break;
                    }
                }
                if (flag2)
                { // 在flag1已通过的基础上，此时flag2通过则代表此时的i和j就是找到的鞍点
                    printf("%d %d\n", i, j);
                    answer = 1;
                    break;
                }
            }
        }
        if (answer == 1)
        { // 若answer等于1时则跳出循环
            break;
        }
    }
    if (answer == 0)
    {
        printf("NO\n");
    }
    return 0;
}
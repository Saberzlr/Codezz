/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 11:20
 * @file    :   7_46.C
 * @author  :   Saber
 * @brief   :   爬动的蠕虫
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n, u, d;
    scanf("%d %d %d", &n, &u, &d);

    // 爬井
    int sum = 0, i = 0;
    while (1)
    {
        sum += u;
        i++;

        // 此处判断是因为，只有往上爬才可能满足条件，如果往上爬都不能满足sum >= n，那么往下爬又怎么可能达到呢
        if (sum >= n)
        {
            break;
        }
        sum -= d;
        i++;
    }

    // 输出
    printf("%d", i);

    return 0;
}
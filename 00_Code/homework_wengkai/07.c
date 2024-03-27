/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/27 19:49
 * @file    :   07.c
 * @author  :   Saber
 * @brief   :   求素数和
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int n, m;
    int i;
    int sum = 0;
    scanf("%d %d", &n, &m);
    int cnt = 0;

    // 第200个素数为1229[max]
    // 但是此处 x <= 1229 这个条件也可以不写 => 不写的话记得加上else if，否则无法退出最外层循环
    for (int x = 2; x <= 1229; x++)
    {
        int isPrime = 1;
        for (i = 2; i < x; i++)
        {
            if (x % i == 0)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime)
        {
            cnt++;
            if (n <= cnt && cnt <= m)
            {
                sum += x;
            }
            /* else if (cnt > m)
            {
                break;
            } */
            // printf("%d,%d,%d\n", x, cnt, sum);
        }
    }
    printf("%d", sum);

    return 0;
}
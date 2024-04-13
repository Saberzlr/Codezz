/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/13 16:37
 * @file    :   7_44.c
 * @author  :   Saber
 * @brief   :   黑洞数
 * ***********************************
 */

#include <stdio.h>

int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 找黑洞数
    int a, b, c;
    int count = 0;
    int max_1, max_2, min;
    int v1, v2;
    while (1)
    {
        // 分解三位数
        a = n / 100;
        b = (n / 10) % 10;
        c = n % 10;
        // printf("%d %d %d\n", a, b, c);
        if (a == b && b == c)
        {
            printf("0");
            break;
        }
        else
        {
            // 数字组合
            // 排序方式1 => 复杂
            if (a > b)
            {
                if (a > c)
                {
                    max_1 = a;
                    if (b > c)
                    {
                        max_2 = b;
                        min = c;
                    }
                    else
                    {
                        max_2 = c;
                        min = b;
                    }
                }
                else
                {
                    max_1 = c;
                    max_2 = a;
                    min = b;
                }
            }
            else
            {
                if (a < c)
                {
                    if (b > c)
                    {
                        max_1 = b;
                        max_2 = c;
                        min = a;
                    }
                    else
                    {
                        max_1 = c;
                        max_2 = b;
                        min = a;
                    }
                }
                else
                {
                    max_1 = b;
                    max_2 = a;
                    min = c;
                }
            }

            /*
            // 排序方式2 => 简便
            // 这三条语句的目的是为了使  a<b<c  方便表示重排求差的过程
            int t;
            if (a > b)
            {
                t = a;
                a = b;
                b = t;
            }
            if (a > c)
            {
                t = a;
                a = c;
                c = t;
            }
            if (b > c)
            {
                t = b;
                b = c;
                c = t;
            }
            */

            // printf("%d %d %d", max_1, max_2, min);

            v1 = max_1 * 100 + max_2 * 10 + min;
            v2 = min * 100 + max_2 * 10 + max_1;

            // 第几轮
            count++;

            // 输出
            printf("%d: %d - %d = %d\n", count, v1, v2, v1 - v2);

            // 判断是否找到黑洞数，找到 => 跳出循环
            if (v1 - v2 == 495)
            {
                break;
            }

            // 更新要分解的数字
            n = v1 - v2;
        }
    }

    return 0;
}
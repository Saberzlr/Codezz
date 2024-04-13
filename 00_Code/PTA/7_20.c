/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/13 15:46
 * @file    :   7_20.c
 * @author  :   Saber
 * @brief   :   简单计算器
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n;
    char ch;
    scanf("%d", &n); // 1
    // 判断while循环是否是因为出错而退出的
    // 0 => 因出错而退出循环
    // 1 => 正常退出循环
    int isFalse = 0;

    // 计算
    int t;
    while (1)
    {
        // 输入OP
        scanf("%c", &ch); // + * - / =
        // 判断是否要结束
        if (ch == '=')
        {
            break;
        }

        // 暂存上一轮n的值
        t = n; // 1 3 30 20
        // 输入这一轮n的值
        scanf("%d", &n); // 2 10 10 2

        // 判断应该做什么操作
        if (ch == '+')
        {
            n = t + n; // 3
        }
        else if (ch == '-')
        {
            n = t - n; // 20
        }
        else if (ch == '*')
        {
            n = t * n; // 30
        }
        else if (ch == '/')
        {
            if (n == 0)
            {
                printf("ERROR");
                isFalse = 1;
                break;
            }
            n = t / n; // 10
        }
        else
        {
            printf("ERROR");
            isFalse = 1;
        }
    }

    // 输出
    if (isFalse == 0)
    {
        printf("%d", n);
    }

    return 0;
}
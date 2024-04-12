/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/12 12:45
 * @file    :   7_39.c
 * @author  :   Saber
 * @brief   :   龟兔赛跑
 * ***********************************
 */

// 乌龟 => 3m/min
// 兔子 => 9m/min => 每10min看一次乌龟 => 如果超过乌龟 => 休息30min
//                                       否则        => 跑10min

/*
#include <stdio.h>
int main()
{   // 方法1
    // 输入
    int t;
    scanf("%d", &t);
    int tort = 0, rabbit = 0;

    // 赛跑
    int i;
    tort = 3 * t;
    for (i = 1; i <= t; i++)
    {
        if (i % 10 == 0 && rabbit > 3 * i)
        {
            i += 3 * 10;
        }
        rabbit += 9;
    }

    // 输出
    if (tort > rabbit)
    {
        printf("@_@ %d", tort);
    }
    else if (tort < rabbit)
    {
        printf("^_^ %d", rabbit);
    }
    else
    {
        printf("-_- %d", tort);
    }

    return 0;
}
*/
// 方法2
#include <stdio.h>
int main()
{
    // 输入
    int t;
    scanf("%d", &t);
    int tort = 0, rabbit = 0;

    // 赛跑
    int rest = 0;
    for (int i = 0; i < t; i++)
    {
        // 乌龟一直跑
        tort += 3;

        if (i % 10 == 0 && rest == 0 && rabbit > tort)
        {
            // 兔子发现自己跑得比乌龟快
            // 休息30min
            if (rabbit > tort)
            {
                rest = 30;
            }
        }

        // 如果兔子不休息 => 继续跑步
        if (rest == 0)
        {
            rabbit += 9;
        }
        // 如果兔子还在休息 => 不跑步 => 休息时间--
        else
        {
            rest--;
        }
    }

    // 输出
    if (tort > rabbit)
    {
        printf("@_@ %d", tort);
    }
    else if (tort < rabbit)
    {
        printf("^_^ %d", rabbit);
    }
    else
    {
        printf("-_- %d", tort);

        return 0;
    }
}
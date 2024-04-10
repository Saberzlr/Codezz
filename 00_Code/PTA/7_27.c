/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/08 14:56
 * @file    :   7_27.c
 * @author  :   Saber
 * @brief   :   兔子繁衍问题
 * ***********************************
 */

// 1 -> 1small          ->  1
// 2 -> 1small          ->  1
// 3 -> 1big + 1small   ->  2
// 4 -> 1big + 2small   ->  3
// 5 -> 2big + 3small   ->  5
// 6 -> 3big + 5small   ->  8
// 7 -> 5big + 8small   ->  13
// 经分析 => 本题是斐波那契数列问题的变种
// a  b  c
// 1
// 1  1
// 1  1  2
// 1  2  3
// 2  3  5
#include <stdio.h>

int fib(int n)
{
    if (n == 1 || n == 2)
    {
        return 1;
    }
    else
    {
        return fib(n - 1) + fib(n - 2);
    }
}
int main()
{
    int N;
    int res;
    scanf("%d", &N);

    int i;
    for (i = 1; i < 100; i++)
    {
        res = fib(i);
        if (fib(i) >= N)
        {
            break;
        }
    }

    printf("%d", i);

    return 0;
}
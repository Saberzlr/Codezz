/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 19:34
 * @file    :   7_31.c
 * @author  :   Saber
 * @brief   :   掉入陷阱的数字
 * ***********************************
 */

#include <stdio.h>
double a3, a2, a1, a0; // 跨函数的变量弄成全局变量

double f(double x)
{
    return a3 * x * x * x + a2 * x * x + a1 * x + a0;
}

int main()
{
    double a, b, mid;
    scanf("%lf %lf %lf %lf", &a3, &a2, &a1, &a0);
    scanf("%lf %lf", &a, &b);
    while (b - a >= 1e-4 && f(a) * f(b) <= 0)
    { // 1e-4是 10 的 -4 次方
        if (f(a) == 0)
        {            // 某个时间结束，而不是无限进行下去，不加会TLE
            mid = a; // mid代表是根
            break;
        }
        if (f(b) == 0)
        {
            mid = b;
            break;
        }
        mid = (a + b) / 2;
        if (f(mid) == 0)
        {
            break;
        }
        else
        {
            if (f(mid) * f(a) >= 0)
            {
                a = mid;
            }
            else
            {
                b = mid;
            }
        }
    }
    printf("%.2f", mid);
    return 0;
}
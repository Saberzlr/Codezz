/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/08 16:29
 * @file    :   02_example02.c
 * @author  :   Saber
 * @brief   :   多项式求和
 * ***********************************
 */

#include <math.h>
#include <stdio.h>

double f1(int n, double a[], double x)
{
    int i;
    double p = a[0];
    for (i = 1; i <= n; i++)
        p += a[i] * pow(x, i);
    return p;
}

int main()
{
    int n;        // 项数
    double x;     // 底数
    double a[99]; // 系数
    scanf("%d %lf", &n, &x);
    for (int i = 0; i < n; i++)
        scanf("%lf", &a[i]);
    for (int i = 0; i < n; i++)
        printf("%lf", &a[i]);

    // double res = f(n, a, x);
    // printf("%f", res);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/04 17:07
 * @file    :   04_example04.c
 * @author  :   Saber
 * @brief   :   再试一个多项式[课后讨论]
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
#include <time.h>
clock_t start, stop;
double duration;
#define MAX_N 100 // 多项式最大项数，即多项式[阶数 + 1]
#define MAX_K 1e6
double f1(int n, double a[], double x);
double f2(int n, double a[], double x);

// 计算f(x) = 1 + x^1 / 1 + x^2 / 2 + ... + x^i / i + x^100 /100 在x = 1.1处的值
int main()
{
    int i;
    // 存储多项式的系数
    double a[MAX_N];
    a[0] = 1;
    for (i = 1; i < MAX_N; i++)
    {
        a[i] = (double)i;
    }

    // 测f1函数的运行时间
    start = clock();
    // 循环多次执行 -> 因为时间太短，显示不出来
    for (int i = 0; i < MAX_K; i++)
    {
        f1(MAX_N - 1, a, 1.1);
    }
    stop = clock();
    // 计算函数单次运行的时间
    duration = ((double)(stop - start)) / CLK_TCK / MAX_K;
    printf("ticks1 = %f\n", ((double)(stop - start)) / CLK_TCK);
    printf("f1函数的运行时间为: %6.2e\n", duration);
    printf("%f\n", f1(MAX_N - 1, a, 1.1));

    // 测f2函数的运行时间
    start = clock();
    // 循环多次执行 -> 因为时间太短，显示不出来
    for (int i = 0; i < MAX_K; i++)
    {
        f2(MAX_N - 1, a, 1.1);
    }
    stop = clock();
    // 计算函数单次运行的时间
    duration = ((double)(stop - start)) / CLK_TCK / MAX_K;
    printf("ticks2 = %f\n", ((double)(stop - start)) / CLK_TCK);
    printf("f2函数的运行时间为: %6.2e\n", duration);
    printf("%f\n", f2(MAX_N - 1, a, 1.1));

    return 0;
}

// 一般方法
double f1(int n, double a[], double x)
{
    int i;
    double p = a[0];
    for (i = 1; i <= n; i++)
    {
        p += (1 / a[i]) * pow(x, i);
    }
    return p;
}

// 秦九韶算法
double f2(int n, double a[], double x)
{
    int i;
    double p = 1 / a[n];
    for (i = n; i > 0; i--)
    {
        p = (1 / a[i - 1]) + x * p;
    }
    return p;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/04 17:26
 * @file    :   test.c
 * @author  :   Saber
 * @brief   :
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
#include <time.h>
clock_t start, stop;
double duration;
#define MAX_N 5 // 多项式最大项数，即多项式[阶数 + 1]
#define MAX_K 1e6
double f1(int n, double a[], double x);
double f2(int n, double a[], double x);

// 计算f(x) = 1 + x^1 / 1 + x^2 / 2 + ... + x^i / i + x^100 /100 在x = 1.1处的值
int main()
{
	int i;
	// 存储多项式的系数
	double a[MAX_N];
	// a[0] = 1;
	for (i = 0; i < MAX_N; i++)
	{
		a[i] = (double)i;
	}

	printf("%f\n", f1(MAX_N - 1, a, 1.1));
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
		p += a[i] * pow(x, i);
	}
	return p;
}

// 秦九韶算法
double f2(int n, double a[], double x)
{
	int i;
	double p = a[n];
	for (i = n; i > 0; i--)
	{
		p = a[i - 1] + x * p;
	}
	return p;
}
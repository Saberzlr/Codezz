/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/08 16:26
 * @file    :   01_example01.c
 * @author  :   Saber
 * @brief   :   PrintN函数的实现
 * ***********************************
 */

#include <stdio.h>

void PrintN1(int N)
{
	int i;
	for (i = 1; i <= N; i++)
	{
		printf("%d\n", i);
	}
}

void PrintN2(int N)
{
	if (N)
	{
		PrintN2(N - 1);
		printf("%d\n", N);
	}
}

int main()
{
	int N;
	scanf("%d", &N);
	PrintN1(N);
	// 递归程序对空间占用太大了
	// 解决问题方法的效率，跟空间的利用效率有关
	PrintN2(N); // 若N = 100000，则会报错

	return 0;
}

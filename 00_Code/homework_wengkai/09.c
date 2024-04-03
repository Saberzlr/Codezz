/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/03 18:55
 * @file    :   09.c
 * @author  :   Saber
 * @brief   :   高精度小数
 * ***********************************
 */

#include <stdio.h>

const int N = 200;
int main()
{
    // 输入
    int v1, v2;  // 被除数 和 除数
    int res;     // 存储商
    int a[N];    // 定义数组存储结果
    int cnt = 0; // 计数器
    int t = 1;   // 存储余数
    scanf("%d/%d", &v1, &v2);

    // 先输出0.
    printf("0.");
    // 初步处理被除数
    v1 = v1 * 10;
    while (t != 0 && cnt < N)
    {
        // 存储商
        res = v1 / v2;
        // 存储余数
        t = v1 % v2;
        // 处理余数
        v1 = t * 10;

        // 将结果存到数组中
        a[cnt] = res;
        cnt++;
    }

    // 输出
    for (int i = 0; i < cnt; i++)
    {
        printf("%d", a[i]);
    }
    printf("\n");

    return 0;
}
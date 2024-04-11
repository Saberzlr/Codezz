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
int main()
{
    // 输入
    int n;
    scanf("%d", &n);

    // 掉入陷阱
    int cnt = 0;
    int temp = 3;
    while (1)
    {
        int sum = 0; // 用于存储和
        int a;       // 用于存储分解的数字
        int temp;    // 用于作比较

        temp = n;
        cnt++;

        while (n)
        {
            a = n % 10;
            n /= 10;
            sum += a;
        }
        n = sum * 3 + 1;

        printf("%d:%d\n", cnt, n);
        if (temp == n)
        {
            break;
        }
    }

    return 0;
}
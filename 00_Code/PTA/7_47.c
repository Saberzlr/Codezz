/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 11:33
 * @file    :   7_47.c
 * @author  :   Saber
 * @brief   :   二进制的前导的零
 * ***********************************
 */

#include <stdio.h>
const int N = 32;
int arr[N];
int main()
{
    // 输入
    int n, res;
    scanf("%d", &n);

    // 十进制 -> 二进制
    if (n >= 0)
    {
        for (int i = 0; n != 0; i++)
        {
            arr[i] = n % 2;
            n /= 2;
        }

        for (int i = 31; i >= 0; i--)
        {
            if (arr[i] == 1)
            {
                res = 32 - i - 1;
                break;
            }
            else
            {
                // 32个数全为0 => 即n = 0的情况，前导32个0
                res = 32;
            }
        }
    }
    else
    {
        res = 0;
    }

    // 输出
    printf("%d", res);

    return 0;
}
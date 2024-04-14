/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/10 18:33
 * @file    :   test.c
 * @author  :   Saber
 * @brief   :   测试
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int n, res;
    scanf("%d", &n);
    int arr[32] = {0};

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
                res = 31 - i;
                break;
            }
        }
        // 32个数全为0 => 即n = 0的情况，前导32个0
        res = 32;
    }
    else
    {
        res = 0;
    }

    // 输出
    printf("%d", res);

    return 0;
}
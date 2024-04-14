/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/14 18:09
 * @file    :   7_55.c
 * @author  :   Saber
 * @brief   :   查询水果价格
 * ***********************************
 */

#include <stdio.h>
int main()
{
    int cnt = 0;

    // 打印菜单
    printf("[1] apple\n");
    printf("[2] pear\n");
    printf("[3] orange\n");
    printf("[4] grape\n");
    printf("[0] exit\n");

    int exit;
    while (1)
    {
        exit = 0;
        // 输入
        int n;
        scanf("%d", &n);
        double price;
        cnt++;

        switch (n)
        {
        case 0:
            exit = 1;
            break;
        case 1:
            price = 3.0;
            break;
        case 2:
            price = 2.5;
            break;
        case 3:
            price = 4.1;
            break;
        case 4:
            price = 10.2;
            break;
        default:
            price = 0;
            break;
        }

        // 判断是否要退出
        if (exit == 1 || cnt > 5)
        {
            break;
        }

        // 输出
        printf("price = %.2f\n", price);
    }

    return 0;
}
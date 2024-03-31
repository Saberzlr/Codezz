/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 21:38
 * @file    :   7_18.c
 * @author  :   Saber
 * @brief   :   出租车计价
 * ***********************************
 */

// 拓展：C语言中四舍五入的方法[一位小数点]
// (int)(a + 0.5)
#include <stdio.h>
int main()
{
    // 输入
    double mile, price;
    int min;
    scanf("%lf %d", &mile, &min);

    // 计算
    // 1. 不同 行驶里程 产生的 价钱
    if (mile <= 3)
    {
        price = 10;
    }
    else if (mile > 3 && mile <= 10)
    {
        price = 10 + 2 * (mile - 3);
    }
    else
    {
        price = 10 + 3 * (mile - 10) + 2 * 7;
    }
    // 2. 等待时间 产生的价钱
    price += 2 * (min / 5);

    // 输出
    printf("%d", (int)(price + 0.5));

    return 0;
}
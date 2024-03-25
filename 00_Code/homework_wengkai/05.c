/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/25 19:26
 * @file    :   05.c
 * @author  :   Saber
 * @brief   :   奇偶个数
 * ***********************************
 */

#include <stdio.h>
int main()
{
    /**
     * @brief
     * 1. 读入一系列数据，-1是结束标志 => 循环必须要执行一次 => do...while循环
     * 2. 定义num变量用来接收输入的数据
     * 3. 判断奇数和偶数的个数 => 定义count1、count2两个变量，初始化位0
     * 4. 每输入一个数字就判断是否为偶数 => if (num % 2 == 0) => 偶数，count1++
     * 5. 否则为偶数 => count2++
     */
    int num;
    int count1 = 0, count2 = 0;
    do
    {
        scanf("%d", &num);
        if (num == -1)
        {
            break;
        }
        else
        {
            if (num % 2 != 0)
            {
                count1++;
            }
            else
            {
                count2++;
            }
        }
    } while (num != -1);
    printf("%d %d", count1, count2);

    return 0;
}
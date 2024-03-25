/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/25 19:26
 * @file    :   06.c
 * @author  :   Saber
 * @brief   :   数字特征值
 * ***********************************
 */

#include <math.h>
#include <stdio.h>
int main()
{
    /**
     * @brief
     * 1. 定义num变量来接收输入的数字
     * 2. 分离数字 => while循环
     * 3. 分离数字的同时定义一个count变量，初始值为1，每成功分离一位，则count++
     * 4. 分离的同时，判断count和分离出的数字的奇偶性
     * 5. 若奇偶性相同 => 记录为1，反之记录为0 => 定义临时变量temp来存储
     * 6. 将二进制转为十进制 => sum += temp * 2 ^ (count - 1)
     * 以下是优化过后的代码
     */
    int num, count = 0;
    int sum = 0;
    scanf("%d", &num);
    while (num > 0)
    {
        int digital = num % 10;
        num = num / 10;
        count++;
        // if ((digital % 2 == 0 && count % 2 == 0) || (digital % 2 != 0 && count % 2 != 0))
        if ((digital + count) % 2 == 0)
        {
            sum += 1 * pow(2, (count - 1));
        }
    }
    printf("%d", sum);

    return 0;
}
/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/07 18:28
 * @file    :   7_24.c
 * @author  :   Saber
 * @brief   :   猜数字游戏 -> 二逼题，条件压根不明确，畜生题
 * ***********************************
 */

#include <stdio.h>
int main()
{
    // 输入
    int N;   // 猜测次数
    int KEY; // 游戏产生的随机数
    int num; // 玩家猜测的数字
    int cnt = 0;
    scanf("%d %d", &KEY, &N);

    // 猜数字过程
    do
    {
        scanf("%d", &num);
        cnt++;
        if (num <= 0 || cnt > N)
        {
            printf("Game Over\n");
            break;
        }
        else
        {
            if (num > KEY)
            {
                printf("Too big\n");
            }
            else if (num < KEY)
            {
                printf("Too small\n");
            }
            else
            {
                if (cnt == 1)
                {
                    printf("Bingo!\n");
                    break;
                }
                else if (cnt <= 3)
                {
                    printf("Lucky You!\n");
                }
                else if (cnt <= N)
                {
                    printf("Good Guess!\n");
                }
                else
                {
                    printf("Game Over");
                    break;
                }
            }
        }
    } while (num > 0);

    return 0;
}
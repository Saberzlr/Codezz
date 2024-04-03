/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/04/03 17:48
 * @file    :   09_tic_tac_toe .c
 * @author  :   Saber
 * @brief   :   井字棋游戏 - 难
 * ***********************************
 */

#include <stdio.h>

const int size = 3; // 棋盘尺寸
// 胜利条件: -1 => 没人赢，0 => O赢，1 => X赢
int main()
{
    int board[size][size];        // 棋盘矩阵
    int i, j;                     // 行和列
    int numOfX, numOfX1, numOfX2; // X的个数
    int numOfO, numOfO1, numOfO2; // O的个数
    int result = -1;              // 是否达成胜利条件(3个X 或 3个O)

    // 读入棋盘矩阵
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            scanf("%d", &board[i][j]);
        }
    }

    // 打印棋盘矩阵
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            printf("%d ", board[i][j]);
            if (j == size - 1)
            {
                printf("\n");
            }
        }
    }

    /*
        // 分别检查 - 行
        for (i = 0; i < size && result == -1; i++)
        {
            numOfO = numOfX = 0;
            for (j = 0; j < size; j++)
            {
                if (board[i][j] == 1)
                {
                    numOfX++;
                }
                else
                {
                    numOfO++;
                }
            }
            if (numOfX == size)
            {
                result = 1;
            }
            else if (numOfO == size)
            {
                result = 0;
            }
        }

        // 分别检查 - 列
        for (j = 0; j < size && result == -1; j++)
        {
            numOfO = numOfX = 0;
            for (i = 0; i < size; i++)
            {
                if (board[i][j] == 1)
                {
                    numOfX++;
                }
                else
                {
                    numOfO++;
                }
            }
            if (numOfX == size)
            {
                result = 1;
            }
            else if (numOfO == size)
            {
                result = 0;
            }
        }
    */

    // 同时检查 - 行和列
    for (i = 0; i < size && result == -1; i++)
    {
        numOfO = numOfX = numOfX1 = numOfO1 = 0;
        for (j = 0; j < size; j++)
        {
            if (board[i][j] == 1)
            {
                numOfX++;
            }
            else
            {
                numOfO++;
            }
            if (board[j][i] == 1)
            {
                numOfX1++;
            }
            else
            {
                numOfO1++;
            }
        }
        if (numOfX == size || numOfX1 == size)
        {
            result = 1;
        }
        else if (numOfO == size || numOfO1 == size)
        {
            result = 0;
        }
    }
    /*
        // 分别检查 - 正对角线
        numOfO = numOfX = 0;
        for (i = 0; i < size; i++)
        {
            if (board[i][i] == 1)
            {
                numOfX++;
            }
            else
            {
                numOfO++;
            }
            if (numOfO == size)
            {
                result = 0;
            }
            else if (numOfX == size)
            {
                result = 1;
            }
        }

        // 分别检查 - 反对角线
        numOfO = numOfX = 0;
        for (i = 0; i < size; i++)
        {
            if (board[i][size - i - 1] == 1)
            {
                numOfX++;
            }
            else
            {
                numOfO++;
            }
            if (numOfO == size)
            {
                result = 0;
            }
            else if (numOfX == size)
            {
                result = 1;
            }
        }
    */

    // 检查对角线
    numOfO = numOfX = numOfO2 = numOfX2 = 0;
    for (i = 0; i < size; i++)
    {
        if (board[i][i] == 1)
        {
            numOfX++;
        }
        else
        {
            numOfO++;
        }
        if (board[i][size - i - 1] == 1)
        {
            numOfX2++;
        }
        else
        {
            numOfO2++;
        }

        if (numOfO == size || numOfO2 == size)
        {
            result = 0;
        }
        else if (numOfX == size || numOfX2 == size)
        {
            result = 1;
        }
    }

    // 输出结果
    if (result == 1)
    {
        printf("X赢");
    }
    else if (result == 0)
    {
        printf("O赢");
    }
    else if (result == -1)
    {
        printf("平局");
    }

    return 0;
}
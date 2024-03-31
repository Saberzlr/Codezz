/**
 * ***********************************
 * @version :   1.0
 * @date    :   2024/03/31 20:24
 * @file    :   7_11.c
 * @author  :   Saber
 * @brief   :   计算平均分
 * ***********************************
 */

#include <stdio.h>
struct score
{
    int math;
    int eng;
    int comp;
};
typedef struct score Score;
int main()
{
    int avg;
    Score stu = {87, 72, 93};

    avg = (stu.math + stu.eng + stu.comp) / 3;

    printf("math = %d, eng = %d, comp = %d, average = %d", stu.math, stu.eng, stu.comp, avg);

    return 0;
}
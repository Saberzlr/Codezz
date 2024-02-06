#include <stdio.h>
// 4.枚举常量

enum Color
{
    // 枚举常量
    RED,
    GREEN,
    BLUE
};

int main()
{
    // 三原色
    /**
     * 创建对象
     * 创建变量的时候才会向内存申请空间
     * 而创建常量的时候不会向内存申请空间
     *
     * enum Color c = RED;就是向内存申请空间
     * enum Color {...} 只是一个类型
     * */
    enum Color c = RED;

    return 0;
}
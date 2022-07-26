// My Answer
#include <stdio.h>

int main()
{
    float a, b;
    printf("Please enter two separate data\n");
    scanf("%f", &a);
    scanf("%f", &b);
    if (a > b)
        printf("a is bigger than b");
    else
        printf("b is bigger than a");
    return 0;
}
// Standard Answer
// two numbers
#include <stdio.h>

int main()
{
    int a, b;

    a = 11;
    b = 99;

    // 也可以通过以下代码实现让用户在终端输入两个数
    // printf("输入第一个值:");
    // scanf("%d", &a);
    // printf("输入第二个值:");
    // scanf("%d", &b);

    if (a > b)
        printf("a 大于 b");
    else
        printf("a 小于等于 b");

    return 0;
}
// three numbers
#include <stdio.h>

int main()
{
    int a, b, c;

    a = 11;
    b = 22;
    c = 33;

    if (a > b && a > c)
        printf("%d 最大", a);
    else if (b > a && b > c)
        printf("%d 最大", b);
    else if (c > a && c > b)
        printf("%d 最大", c);
    else
        printf("有两个或三个数值相等");

    return 0;
}
// Community Answers
// four numbers
#include <stdio.h>

int main() //用的三目运算符

{
    int a = 5, b = 4, c = 3, d = 6, min;
    min = (((c < d) ? c : d) < ((a < b) ? a : b)) ? ((c < d) ? c : d) : ((a < b) ? a : b);
    printf("最小的数字为：%d", min);
    return 0;
}
// my answer
#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d", a);
    return 0;
}
// standard answer
#include <stdio.h>
int main()
{
    int number;

    // printf() 输出字符串
    printf("输入一个整数: ");

    // scanf() 格式化输入
    scanf("%d", &number);

    // printf() 显示格式化输入
    printf("你输入的整数是: %d", number);
    return 0;
}
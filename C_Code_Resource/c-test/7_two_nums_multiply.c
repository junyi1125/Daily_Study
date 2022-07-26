// my answer
#include <stdio.h>

int main()
{
    float a, b, c;
    printf("enter two nums,separetd with \',\'");
    scanf("%f,%f", &a, &b);
    c = a * b;
    printf("the answer is %f", c);
    return 0;
}
// standard answer
#include <stdio.h>
int main()
{
    double firstNumber, secondNumber, product;
    printf("输入两个浮点数: ");

    // 用户输入两个浮点数
    scanf("%lf %lf", &firstNumber, &secondNumber);

    // 两个浮点数相乘
    product = firstNumber * secondNumber;

    // 输出结果， %.2lf 保留两个小数点
    printf("结果 = %.2lf", product);

    return 0;
}
// my answer
#include <stdio.h>

int main()
{
    float a, b, c;
    printf("please input two nums \nthat u want added together,and separed it with blank space\n");
    scanf("%f %f", &a, &b);
    c = a + b;
    printf("the number is %f", c);
    return 0;
}
// standard answer
#include <stdio.h>
int main()
{
    int firstNumber, secondNumber, sumOfTwoNumbers;

    printf("输入两个数(以空格分割): ");

    // 通过 scanf() 函数接收用户输入的两个整数
    scanf("%d %d", &firstNumber, &secondNumber);

    // 两个数字相加
    sumOfTwoNumbers = firstNumber + secondNumber;

    // 输出结果
    printf("%d + %d = %d", firstNumber, secondNumber, sumOfTwoNumbers);

    return 0;
}
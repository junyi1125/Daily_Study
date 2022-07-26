#include <stdio.h>
#include <math.h>
int main()
{
    double a, b, c, s, area;
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    s = (a + b + c) / 2;
    area = sqrt(s * (s - a)*(s - b)*(s - c));
    printf("a=%f\tb=%f\tc=%f\b", a, b, c);
    printf("area=%f\n", area);
    return 0;
}
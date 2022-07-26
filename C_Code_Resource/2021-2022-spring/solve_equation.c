#include <stdio.h>
#include <math.h>

int main()
{
    double s, x1, x2, a, b, c, rpart, ipart;

    printf("please enter three factors,separated by space\n");
    scanf("%lf %lf %lf", &a, &b, &c);
    if (a == 0)
        printf("a cannot be 0");
    else
    {
        s = pow(b, 2) - 4 * a * c;
    }

    if (s == 0)
    {
        x1 = -b / 2 * a;
        printf("this equation only has one solve\n");
        printf("this solve is %.2lf\n", x1);
    }

    if (s > 0)
    {
        x1 = (-b + sqrt(s)) / 2 * a;
        x2 = (-b - sqrt(s)) / 2 * a;
        printf("this equation has two different solves and they are %.2lf and %.2lf", x1, x2);
    }

    if (s < 0)
    {
        rpart = -b / 2 * a;
        ipart = sqrt(s) / 2 * a;
        printf("this equation has two complex solves\n");
        printf("%.2lf + %.2lf i \n", rpart, ipart);
        printf("%.2lf - %.2lf i \n", rpart, ipart);
    }
}

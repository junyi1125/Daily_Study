#include <stdio.h>
#include <math.h>
int main()
{
    double a, b, c, s, area;
    scanf("%lf%lf%lf", &a, &b, &c);
    if (a + b <= c && a + c <= b && b + c <= a)
    {
        printf("这个三角形不成立");
    }
    else
    {
        s = (a + b + c) / 2;
        area = sqrt(s * (s - a) * (s - b) * (s - c));
        printf("三角形的三边长分别为a=%lf,b=%lf,c=%lf\n", a, b, c);
        printf("三角形的面积为,area=%lf\n", area);
    }
    return 0;
}
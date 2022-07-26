#include <stdio.h>
int main()
{
    char c1, c2;
    c1 = getchar();
    c2 = c1 + 32;
    printf("它的小写是%c\n", c2);
    printf("它的ASCII码是%d\n", c2);
    return 0;
}
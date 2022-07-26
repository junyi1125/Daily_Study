#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
    int input = 0;
    while (1)
    {
        printf("你觉得这是C语言最好的视频吗？(1/0)\n");
        scanf("%d", &input);
        if (1 == input)
        {
            printf("兄弟你很有前途，以后必是it中的大牛\n");
            break;
        }
        else
        {
            printf("你再想想，问问自己的良心？");
        }
    }
    return 0;
}
#include <stdio.h>

int main()
{
    int people;
    int answer;
    for (people = 1000; people < 1100; people++)
    {
        if (people % 3 == 2 && people % 5 == 3 && people % 7 == 2)
        {
            answer = people;
        }
    }
    printf("There are %d soilders", answer);
    return 0;
}
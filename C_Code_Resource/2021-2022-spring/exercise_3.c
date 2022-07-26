#include <stdio.h>
int main()
{
    int year, month, mon;

    printf("Please enter year firstly and month secondly,separated by space\n");
    scanf("%d %d", &year, &month);

    if ((month < 1) || (month > 12))
        printf("The month you enter in is not exist\n");
    else
    {
        if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0))
        {
            mon = 1;
            printf("this year is a leap year\n");
        }
        else
        {
            mon = 2;
            printf("this year is non-leap year\n");
        }
    }

    switch (month)
    {
    case 1:
        printf("January has 31 days");
        break;
    case 2:
        mon == 1 ? printf("February has 29 days") : printf("February has 28 days");
        break;
    case 3:
        printf("March has 31 days");
        break;
    case 4:
        printf("April has 30 days");
        break;
    case 5:
        printf("May has 31 days");
        break;
    case 6:
        printf("June has 30 days");
        break;
    case 7:
        printf("July has 31 days");
        break;
    case 8:
        printf("August has 31 days");
        break;
    case 9:
        printf("September has 30 days");
        break;
    case 10:
        printf("October has 31 days");
        break;
    case 11:
        printf("November has 30 days");
        break;
    case 12:
        printf("December has 31 days");
        break;
    default:
        printf("You entered the wrong month\n");
        break;
    }
}
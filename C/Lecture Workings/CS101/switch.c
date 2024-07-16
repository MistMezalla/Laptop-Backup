#include "stdio.h"
void main()
{
    char col;
    char temp;
    printf("Enter the colour: ");
    scanf("%c",&col);

    switch(col)
    {
        case 'R':
            printf("red");
            break;
        case 'B':
            printf("Blue");
            break;
        default:
            printf("Hi");
    }
}
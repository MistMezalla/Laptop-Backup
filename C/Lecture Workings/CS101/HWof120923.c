#include "stdio.h"
void ascii_hexa()
{
    char ch;
    printf("Enter the character: ");
    scanf("%c",&ch);
    
    if (ch>='\x41'&& ch<='\x5A')
    printf("CL");
    else if(ch>='\x61' && ch<='\x7A')
    printf("SL");
    else if ((ch>='\x0' && ch<='\x1F') || ch=='\x7F')
    printf("Non Printable");
    else if (ch>='\x30' && ch <= '\x39')
    printf("Digit");
    else
    printf("Sp Sym");
}

void non_ascii()
{
    char ch;
    printf("Enter the character: ");
    scanf("%c",&ch);
    
    if (ch>='A'&& ch<='Z')
    printf("CL");
    else if(ch>='a' && ch<='z')
    printf("SL");
    /*else if ((ch>='\x0' && ch<='\x1F') || ch=='\x7F')
    printf("Non Printable");*/
    else if (ch>='0' && ch <= '9')
    printf("Digit");
    else
    printf("Sp Sym");
}

void ascii_decimal()
{
    char ch;
    printf("Enter the character: ");
    scanf("%c",&ch);
    
    if (ch>=65 && ch<=80)
    printf("CL");
    else if(ch>='\x61' && ch<='\x7A') // To reasearch on binary notation
    printf("SL");
    else if ((ch>='\x0' && ch<='\x1F') || ch=='\x7F')
    printf("Non Printable");
    else if (ch>='\x30' && ch <= '\x39')
    printf("Digit");
    else
    printf("Sp Sym");
}
void main()
{
    //ascii_hexa();
    //non_ascii();
    ascii_decimal();
}
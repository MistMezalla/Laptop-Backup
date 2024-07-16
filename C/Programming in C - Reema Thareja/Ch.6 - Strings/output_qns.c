#include <stdio.h>
#include <string.h>

void Q1()
{
    char str1[]={'h','i'};
    char str2[]={'h','i','\0'};
    char str3[]="Hello World";
    char str5[]="hi";

    if (!strcmp(str1,str2))
        printf("Equal");
    else
        printf("Non equal");

    if (strstr(str3,"rld"))
        printf("\nFound");

    printf("\n%d",strcmp(str1,str2));
    printf("\n%d",*strstr(str3,"Wor")); 
    printf("\n%d",'W');
    printf("\n%s",str1);
}

void Q2()
{
    char str4[]="Hello World";
    int i;
    while(str4[i]!='\0')
    {
        if (i%2==0)
            printf("%c ",str4[i]);
        i++;
    }
}
void main()
{
    Q1();
}
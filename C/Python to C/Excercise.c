#include <stdio.h>
#include <string.h>
void Q2e()
{
    char first[10]={};
    char middle[10]={};
    char last[10]={};
    char fullname[30]={};
    printf("Enter the first name: ");
    //scanf("%c",&first);
    fgets(first,sizeof(first),stdin);
    printf("%s",first);
    printf("Enter the middle name: ");
    //scanf("%c",&middle);
    fgets(middle,sizeof(middle),stdin);
    printf("Enter the last name: ");
    //scanf("%c",&last);
    fgets(last,sizeof(last),stdin);
    printf("%s%s%s",first,middle,last);
    
    strcat(fullname,first);
    strcat(fullname,middle);
    strcat(fullname,last);
    printf("%s",fullname);
}   


void trial()
{
    int a,b;
    scanf("%3d%5d",&a,&b);
    printf("%d\n%d",a,b);
}
void main()
{
        Q2e();
}
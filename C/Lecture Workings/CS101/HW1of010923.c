#include<stdio.h>
void main()
{
    int a,b,c;
    
    printf("Enter the first number: ");
    scanf("%d",&a);
    printf("Enter the second number: ");
    scanf("%d",&b);
    c=a;
    a=b;
    b=c;
    /*a,b=b,a;*/
    printf("The first number is: %d\n",a);
    printf("The second number is: %d",b);
}

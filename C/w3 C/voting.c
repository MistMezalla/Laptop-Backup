#include <stdio.h>
void main()
{
    int a;
    printf("Enter your age: ");
    scanf("%d",&a);

    if (a>=18){
        printf("Eligible to vote");
    }
    else if(a>=0 && a<18){
        printf("Ineligible to vote");
    }else{
        printf("Enter a positive integer");
    }
}
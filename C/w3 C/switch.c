#include <stdio.h>
void main()
{
    int a;
    scanf("%d",&a);
    int b=a>=18;
    int c=(a<18 && a>0);
    int d=(a<0);

     switch(a){
        case 20:
        printf("Eligible\n");
        break;
        case 10:
        printf("Ineligible\n");
        break;
        case -3:
        printf("Enter a positive integer\n");
        break;
        default:
        printf("Welcome to this world\n");
     }
}
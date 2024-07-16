#include<stdio.h>
void main()
{
    int n1,n2,t;
    printf("Enter the first number: ");
    scanf("%d",&n1);
    printf("Enter the second number: ");
    scanf("%d",&n2);

    if(n1>=n2){
        while((n1%n2)!=0){
            t=n1%n2;
            n1=n2;
            n2=t;
        }
    }
    else{
       while((n2%n1)!=0){
            t=n2%n1;
            n2=n1;
            n2=t; 
        }
    }   
    printf("%d","The gcd is: ",n2);
}



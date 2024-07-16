#include<stdio.h>
#include<stdbool.h>
void main()
{
    int n1,n2,t,c;
    c=0;
    while(c==0){    
        printf("Enter the first number: ");
        scanf("%d",&n1);
        printf("Enter the second number: ");
        scanf("%d",&n2);
        
    
    
    if(n1>=n2){
        while(!((n1%n2)==0)){
            t=n1%n2;
            n1=n2;
            n2=t;
        }
    printf("The gcd is: %d",n2);
    }
    else{
       while(!((n2%n1)==0)){
            t=n2%n1;
            n2=n1;
            n1=t; 
        }
    printf("The gcd is: %d\n",n1);
    }   
    /*printf("\n");*/
    scanf("%d",&c);
    }

}



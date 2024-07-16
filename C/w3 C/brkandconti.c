#include<stdio.h>
void main()
{
    int i;
    for(i=1;i<=20;i+=2){
        if (i==15){
            break;
        }
        else if((i==5) || (i==3)){
            printf("Hello\t");
            continue;
            printf("Hi");
        }   
    printf("%d\n",i);
    }
}
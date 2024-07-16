#include<stdio.h>
void main()
{
    int i;
    for(i=1;i<=10;i+=2){
        if (i==9){
            break;
        }
        else if(i==5){
            continue;
        }
    printf("%d\n",i);
    }
}

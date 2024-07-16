#include<stdio.h>

void main()
{
    printf("%d\n",a);
    int i,arr[3]={5};
    for(i=0;i<3;++i)
        {
        printf("%d",i);
        printf("\n%d\t%d\n",arr[++i],i);
        }
}
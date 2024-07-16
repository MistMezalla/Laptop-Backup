#include<stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

void Q1_2()
{
    int arr[]={1,2,3,4,5};
    int *ptr,i;
    ptr=arr+4;
    for(i=4;i>=0;i--)
        printf("%d ",*(ptr-i));

    printf("\n");
    for(i=0;i<5;i++)
        printf("%d ",*(ptr-i));
        

}

void Q3_5()
{
    int val=3;
    int *pval=&val;
    printf("%d %d\n",val,*pval);
    printf("%d %d\n",val,*pval++);
    printf("%d %d\n",val,++*pval);
}

void Q6_7()
{
    int arr[]={1,2,3,4,5};
    printf("%d",++*arr);
    int *parr=arr+2;
    printf("\n%d %d",++*parr-1,1+*--parr);
}

void Q8()
{
    int num=5,*ptr=&num,x=*ptr;
    printf("%d %d %d",++num,x+2,*ptr--);
}

void test()
{
    int t=10,*p=&t;
    ++t;
    printf("%d %d\n",t,*p);
}

void test1()
{
    int t=10,*p=&t;
    printf("%d %d %d",++t,t-2,*p);
    printf("\n%d %d",t,*p);
}

void main()
{
    Q8();
}
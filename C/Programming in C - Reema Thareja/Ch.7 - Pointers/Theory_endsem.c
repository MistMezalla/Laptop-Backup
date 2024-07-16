#include <stdio.h>
#include <stdlib.h>

void test1()
{
    int a=10;
    int b=20;

    int *p,*q;
    p=&a;
    q=&b;
    printf("%d,%d\n",*p,*q);
    printf("%d,%d\n",p,q);
    *p++=*q++;
    printf("%d,%d",*p,*q);
}

void test2()
{
    int *arr,n;
    printf("Value of n: ");
    scanf("%d",&n);
    arr=(int*)calloc(n,sizeof(int));

    if (arr==NULL)
        exit(0);
    int i;
    for (i=0;i<n;i++)
        //scanf("%d",&arr[i]);
    for (i=0;i<n;i++)
        printf("%d,",*(arr+i));
    free(arr);
}
void main()
{
    test2();
}
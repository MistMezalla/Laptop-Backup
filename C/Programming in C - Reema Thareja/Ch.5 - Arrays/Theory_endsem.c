#include <stdio.h>

void test1()
{
    int arr[][2]={1,2,3,4,5,6};
    int i,j;
    for (i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
            printf("%d\t",arr[i][j]);
        printf("\n");
    }
    printf("%d",arr[0][5]);
}

void test2()
{
    int i,arr[10];
    for (i=0;i<10;i++)
        arr[i*2]=1;
    for (i=0;i<10;i++)
        arr[i*2+1]=-1;
    for (i=0;i<10;i++)
    printf("%d ",arr[i]);
}
void main()
{
    test2();
}
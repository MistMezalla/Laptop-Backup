#include <stdio.h>

void insertion_sort(int a[])
{
    int i,j;
    for(i=1;i<6;i++)
    {
        j=i-1;
        int key=a[i];
        while(j>-1 && a[j]>=key)
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
    }
}

void main()
{
    int arr[6]={5,0,2,-1,6,4};
    int i;
    for(i=0;i<6;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");

    insertion_sort(arr);
    for(i=0;i<6;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}
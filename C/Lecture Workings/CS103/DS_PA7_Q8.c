#include <stdio.h>

int Partition(int a[],int p,int r)
{
    int x=a[r];
    int i,j;
    i=p-1;
    for (j=p;j<r;j++)
    {
        if (a[j]<=x)
        {
            i++;
            int temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    int temp=a[i+1];
    a[i+1]=a[r];
    a[r]=temp;
    }
    return i+1;
}

void Quicksort(int a[],int p,int r)
{
    int q;
    if(p<r)
    {
        q=Partition(a,p,r);
        Quicksort(a,p,q-1);
        Quicksort(a,q+1,r);
    }
}

void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    int i;
    for (i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);
    }

    Quicksort(arr,0,n-1);

    for (i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
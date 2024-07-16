#include <stdio.h>

void sort(int a[],int n)
{
    int i;
    int pos;
    for (i=0;i<n;i++)
    {
        if(a[i]<a[i+1])
        {
            pos=i;
            break;
        }
    }
    int j;
    j=pos+1;
    i=pos;
    pos=0;
    int arr[n];
    while(i>-1 && j<n)
    {
        if(a[i]<=a[j])
        {
            arr[pos]=a[i];
            i--;
            pos++;
        }
        else if(a[i]>=a[j])
        {
            arr[pos]=a[j];
            j++;
            pos++;
        }
    }

    while(i>-1)
    {
        arr[pos]=a[i];
            i--;
            pos++;
    }

    while(j<n)
    {
        arr[pos]=a[j];
            j++;
            pos++;
    }

    for (i=0;i<n;i++)
    {
        a[i]=arr[i];
    }
}

void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    printf("Enter the data as per the giv conditions: ");
    int i;
    for(i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);
    }

    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");

    sort(arr,n);
    printf("The sorted array is: \n");
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
}
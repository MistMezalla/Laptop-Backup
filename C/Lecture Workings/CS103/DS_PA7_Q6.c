#include <stdio.h>

void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    int i,j;
    printf("Enter the data of array: ");
    for (i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);
    }
    
    for (i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");

    for (i=0;i<n-1;i++)
    {
        int min_ind=i;
        for(j=i+1;j<n;j++)
        {
            if(arr[j]<=arr[min_ind])
            min_ind=j;
        }
        int temp;
        temp=arr[i];
        arr[i]=arr[min_ind];
        arr[min_ind]=temp;
    }

    for (i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}

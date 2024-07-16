#include <stdio.h>

void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);
    int arr[n];
    int i,j;
    for (i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);
    }

    int swap=1;
    for (i=0;i<n;i++)
    {
        for (j=0;j<n-i-1 && swap;j++)
        {
            if(arr[j]>=arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            else 
                swap=0;
        }
    }

    for (i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
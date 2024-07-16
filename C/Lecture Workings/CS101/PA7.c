#include <stdio.h>

void Q6()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int i;
    int arr[n];
    for (i=0;i<n;i++)
    {
        printf("Enter the number: ");
        scanf(" %d",&arr[i]);
    }

    int j,flag=0;
    int ind=1;
    int unique[n];
    unique[0]=arr[0];
    for (i=0;i<n;i++)
    {
        for (j=0;j<ind;j++)
        {
            if (arr[i]!=unique[j])
            {
                flag=1;
            }
        }
        if (flag)
            {
                printf("%d ",arr[i]);
                unique[ind]=arr[i];
                ind++;
            }
    }

    for (i=0;i<ind;i++)
        printf("%d ",unique[i]);
}
void main()
{
    Q6();
}

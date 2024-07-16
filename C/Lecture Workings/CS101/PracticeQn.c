#include <stdio.h>
void main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d",&n);

    int l[10]={};
    
    int i;
    for (i=1;i<=n;i++)
        l[i-1]=i;
    
    int j;
    for (i=1;i<=4;i++)
    {
        for (j=1;j<=i;j++)
            printf("%d",l[i+j-2]);
        printf("\n");
    }
}


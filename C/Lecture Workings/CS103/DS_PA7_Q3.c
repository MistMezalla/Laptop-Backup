#include <stdio.h>
#include <stdlib.h>

void main()
{
    int *p1=(int *)calloc(10,sizeof(int));
    int *p2=(int *)calloc(10,sizeof(int));
    int d1,d2;
    printf("Enter the coeff of expression for poly 1 in asc order:");
    printf("Enter the degree: ");
    scanf(" %d",&d1);
    int i;
    for (i=0;i<=d1;i++)
    {
        int c;
        scanf(" %d",&c);
        p1[i]=c;
    }

    printf("Enter the coeff of expression for poly 2 in asc order:");
    printf("Enter the degree: ");
    scanf(" %d",&d2);
    for (i=0;i<=d2;i++)
    {
        int c;
        scanf(" %d",&c);
        p2[i]=c;
    }

    int *res=(int *)calloc(10,sizeof(int));
    if (d1>=d2)
    {
        for(i=0;i<=d1;i++)
        {
            res[i]=p1[i]+p2[i];
        }
        for (i=d1;i>0;i--)
        {
            printf("%dx^%d+",res[i],i);
        }
        printf("%d",res[i]);
    }
    else
    {
        for(i=0;i<=d2;i++)
        {
            res[i]=p1[i]+p2[i];
        }   
        for (i=d2;i>0;i--)
        {
            printf("%dx^%d+",res[i],i);
        }
        printf("%d",res[i]);
    }    
}
#include "stdio.h"
void main(
{
    int n,i,j;
    float sum=0;
    printf("Enter the number: ");
    scanf("%d",&n);

    for (i=1;i<=n;i++)
    {
        int num=1,den=1;
        for (j=1;j<=i;j++)
        {
            num=num*i;
            den=den*j;
        }
    sum=num/den;
    }
    printf("The value is %f",sum);
}

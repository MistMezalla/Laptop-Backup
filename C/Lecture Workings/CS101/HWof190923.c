#include "stdio.h"
void main()
{
    int i,j,n;
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
    sum+=(float)num/den;
    }
    printf("The value is %f",sum);
}

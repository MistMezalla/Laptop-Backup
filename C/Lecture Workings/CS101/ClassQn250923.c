#include <stdio.h>
void main()
{
    int num,n,sum=0;
    printf("Enter the num: ");
    scanf("%d",&num);
    printf("Enter the n: ");
    scanf("%d",&n);

    int i,d,j;
    for (i=n-1;i>=0;i--)
    {
        int multi=1;
        for (j=i;j>=1;j--)
        {
            multi=multi*10;
        }
        printf("%d\n",multi);
        d=num/multi;
        printf("%d\n",d);
        num=num%multi;
        sum+=d;
    }
    printf("%d",sum);
}
#include <stdio.h>
//Q9 of NCERT 11 std Pg 141

void Q9_1()
{
    int i,n,m;
    printf("Enter the number of the lines to be printed: ");
    scanf("%d",&n); 

    if (i%2!=0)
    {
        m=(n+1)/2; //If the value after evaluation is int then m will 
                   //give the desired output. If n=5 then m=3.
                   // However if value is evaluated as float then ceil
                   // floor is taken,i.e, GIF.
        printf("%d\n",m);
    } 
    else
    {
        m=(n)/2;
        printf("%d\n",m);
    }
    
    // For uppper part
    int a,b,c,d=1;
    for (i=m;i>=1;i--)
    {
        for (a=i-1;a>0;a--)
        {
            printf("^");
        }
        for (b=1;b<=d;b+=1)
        {
            printf("*");
        }
        for (c=i-1;c>0;c--)
        {
            printf("&");
        }
        d+=2;
    
        printf("\n");
    }
    // For lower part
    
    int j,e=n-2;
    for (j=1;j<m-1;j++)
    {
        for (a=1;a<=m-j;a++)
        {
            printf("^");
        }
        for (b=e;b>=1;b-=1)
        {
            printf("*");
        }
        for (c=1;c<=m-j-1;c++)
        {
            printf("&");
        }
        e-=2;
    
        printf("\n");
    }
    
        /*
        printf(a*'^'+b*'*'+c*'&');
        a-=1;b+=2;
        c-=1;
        */
}
    
    


void main()
{
    Q9_1();
}
#include <stdio.h>

//Q1;
int *max1(int *,int *,int *);
void Q1()
{
    int x,y,z;
    printf("Enter the numbers: ");
    scanf(" %d %d %d",&x,&y,&z);

    printf("%d",*(max1(&x,&y,&z)));
}

int *max1(int *a,int *b,int *c)
{
    if (*a>=*b && *a>=*c)
        return a;
    else if (*b>=*c)
        return b;
    else 
        return c;
}

//Q2
int check_odd(int *);
void Q2()
{
    int num;
    printf("Enter the number: ");
    scanf(" %d",&num);

    if (check_odd(&num))
        printf("Odd");
    else
        printf("Even");
}

int check_odd(int *n)
{
    if (*n%2==0)
        return 0;
    else 
        return 1;
}

//Q3
int *reverse_number(int *);
void Q3()
{
    int num;
    printf("Enter the number: ");
    scanf(" %d",&num);

    printf("%d",*reverse_number(&num));
}

int *reverse_number(int *n)
{
    int q;
    q=*n;
    int nd=0;
    while(q)
    {
        q/=10;
        nd++;
    }

    int dig[nd];
    q=*n;
    int i;
    for (i=nd-1;i>=0;i--)
    {
        dig[i]=q%10;
        q/=10;
    }

    static int rev=0;
    int b=1;
    for(i=0;i<nd;i++)
    {
        rev+=dig[i]*b;
        b*=10;
    }

    //printf("%d",rev);

    return &rev;
}
void main()
{
    Q3();
}
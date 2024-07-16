#include <stdio.h>
// Theory

//Q3
int *max(int *,int *,int *);
void Q3()
{
    int a,b,c;
    printf("Enter then numbers: ");
    scanf(" %d \n %d \n %d",&a,&b,&c);

    printf("%d\n",&a);
    printf("Max is %d",max(&a,&b,&c));
}

int *max(int *a,int *b,int *c)
{
    if (*a>=*b && *a>=*c)
        return a;
    else if (*b>=*c)
        return b;
    else 
        return c;
}

//Q6to7
int fact(int );
void Q6to7()
{
    int n,r;
    input:
    printf("Enter the values of n and r: ");
    scanf(" %d %d",&n,&r);

    float permu;
    if (n>=r)
        permu=fact(n)/fact(n-r);
    else 
        goto input;
    printf("%f\n",permu);

    float combi;
    if (n>=r)
        combi=fact(n)/(fact(r)*fact(n-r));
    else
        goto input;
    printf("%f",combi);
}

int fact(int n)
{
    int fact=1;
    int i;
    for (i=1;i<=n;i++)
        fact*=i;
    return fact;
}

//Q10
int GCD(int ,int );
void Q10()
{
    int a,b;
    printf("Enter the numbers a and b: ");
    scanf(" %d %d",&a,&b);

    printf("%d",GCD(a,b));
}

int GCD(int a,int b)
{
    int c=a%b;
    if(c==0)
        return b;
    else 
        return (GCD(b,c)); //14%6=2 6%2=0
}

//Q11
int Expo(int a,int b);
void Q11()
{
    int a,b;
    printf("Enter the numbers: ");
    scanf(" %d %d",&a,&b);

    printf("%d",Expo(a,b));
}

int Expo(int a, int b)
{
    if (b==0)
        return 1;
    else
    {
        return (a*Expo(a,--b)); //5*5,4 25*5,3 125*5,2 625,1 
    }
}

//Q12
int fib(int );
void Q12()
{
    int n;
    printf("Enter the number upto which seq is to be found: ");
    scanf(" %d",&n);

    int i;
    for (i=0;i<=n;i++)
        printf("%d\t",fib(i));
}

int fib(int n)
{
    if (n==0)
        return 0;
    else if(n==1)
        return 1;
    else 
        return (fib(n-1)+fib(n-2));
}

//Tower of Hanoi
void move(int n, int A,int B,int C);
void ToH()
{
    int n;
    printf("Enter the number of rings: ");
    scanf(" %d",&n);

    int A=n,B=0,C=0;
    move(n,A,B,C);
}

void move(int n,int A,int B,int C)
{
    if (A==1)
    {
        //swaping A and C
        A=A+C;
        C=A-C;
        A=A-C;
    }
    else
    {
        A-=(n-1);
        B+=n-1;
        
        A=A+C;
        C=A-C;
        A=A-C;

        C+=B;
        B=0;
    }
    printf("%d,%d,%d",A,B,C);
}

//Q11 tail recursion
int facto1(int ,int );
int facto(int n)
{
    return facto1(n,1);
}
int facto1(int n,int res)
{
    if (n==1)
        return res;
    else
        return facto1(n-1,n*res);
}

void Q11_alt()
{
    int n;
    printf("Enter the number whose factorial is to be found: ");
    scanf(" %d",&n);

    printf("%d",facto(n));
}

//Static variabel test
void print(void);
void static_vari_test()
{
    printf("\t");
    print();
    printf("\t");
    print();
    printf("\t");
    print();
}

void print()
{
    static int x=1;
    int y=0;
    x++;
    y++;
    printf("%d,%d",x,y);
}

void main()
{
    static_vari_test();
}


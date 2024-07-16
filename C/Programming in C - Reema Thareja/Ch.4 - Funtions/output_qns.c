#include <stdio.h>

//Q4
int add(int ,int);
void Q4()
{
    int a=2,b=3;
    printf("%d,%d,%d\n",a,b,add(a,b));
    //printf("%d",d);
}

int d;
int add(int m,int n)
{
    printf("Enter the value of d: ");
    scanf(" %d",&d);
    int c;
    c=m+n;
    return c;
}

//Q6
int func(int);
void Q6()
{
    int a=2;
    printf("%d",func(a));
}

int func(int a)
{
    static int t;
    if (a>1)
    {
        t=func(--a);
        printf("%d\n",t);
        return t+1;

    }
    else
        return 0;
}

//Q9
static int add1(int val)
{
    static int Sum;
    printf("%d\t%d\n",&Sum,&val);
    Sum+=val;
    return Sum;
}

void Q9()
{
    int i;
    static int Sum;
    for (i=0;i<10;i++)
        add1(i);
    printf("%d\n",add1(0));
    printf("%d\n",Sum);
    printf("%d\t%d\t%d\n",main,Q9,add1/*&Sum*/);
}
//Q10
void func1(int *);
int a=10;

void Q10()
{
    int a=2;
    printf("%d\n",a);
    func1(&a);
    printf("%d\n",a);
}

void func1(int *a)
{
    *a=20;
}

//Q12
int A;
static int func2()
{
    return ++A;
}

void Q12()
{
    A=10;
    printf("%d\n",func2());
    A*=10;
    printf("%d\n",func2());
}
void main()
{
    Q9();
}
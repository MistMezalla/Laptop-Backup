#include <stdio.h>

//Q1
int fact(int );
int *facto(int *);
int fact_trec(int *);
int fact_rec(int );
void Q1()
{
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);

    printf("%d\n",fact(num));
    printf("%d\n",*(facto(&num)));
    printf("%d\n",fact_trec(&num));
    printf("%d\n",fact_rec(num));
}

int fact(int n)
{
    int i;
    int b=1;
    for(i=n;i>=1;i--)
        b*=i;
    return b;
}

int *facto(int *n)
{
    int i;
    static int f=1;
    for (i=*n;i>=1;i--)
        f*=i;
    return &f;
}

int fact1(int ,int );
int fact_trec(int *n)
{
    fact1 (*n,1);
}

int fact1(int m,int b)
{
    if (m==0)
        return b;
    else
        fact1(m-1,m*b); 
}

int fact_rec(int n)
{
    if (n==0)
        return 1;
    else
       return n*fact_rec(n-1);
}

#include <math.h>
//Q2
float hyp(int ,int );
void Q2()
{
    int a,b;
    printf("Enter the sides: ");
    scanf("%d %d",&a,&b);

    printf("%f",hyp(a,b));
}

float hyp(int a,int b)
{
    return "%f",sqrt(a*a+b*b);
}

//Q5
int is_prime(int );
void Q5()
{
    int n;
    printf("Enter the number: ");
    scanf(" %d",&n);

    if(is_prime(n))
        printf("Prime");
    else
        printf("Non prime");
}

int is_prime(int num)
{
    int i;
    int flag;
    if (num>=0)
    {
        if (num==1)
            return 0;
        else
        {
            for (i=2;i<=num/2;i++)
            {
                if (num%i==0)
                {    
                    flag=0;
                    break;
                }
                else    
                    flag=1;
            }
        }
        if(flag)
            return 1;
        else 
            return 0;
    }
}

//Q9
int rev(int *);
void Q9()
{
	int num;
	printf("Enter the number: ");
	scanf(" %d",&num);

	printf("%d",rev(&num));
}

int rev(int *n)
{
	int nd=0,q;
	q=*n;
	while(q)
	{
		q/=10;
		nd++;
	}

	int dig[nd];
	int d,i;
	q=*n;
	for (i=0;i<nd;i++)
	{
		d=q%10;
		q/=10;
		dig[i]=d;
	}
	
	int rev_num=0;
	int b=1;
	for (i=nd-1;i>=0;i--)
	{
		rev_num+=dig[i]*b;
		b*=10;
	}
	
	return rev_num;
}

//Q10
int a,b;
void swap(int *,int *);
void Q10()
{	
    printf("Enter the two numbers: ");
    scanf(" %d %d",&a,&b);
	swap(&a,&b); 
	printf("%d %d",a,b);
}

void swap(int *x,int *y)
{
	*x=*x+*y;
	*y=*x-*y;
	*x=*x-*y;
}

//Q11
int F(int ,int );
void Q11()
{
	int a,b;
	printf("Enter the numbers: ");
	scanf(" %d %d",&a,&b);
	
	printf("%d",F(a,b));
}

int F(int x,int y)
{
	if (x<y)
		return 0;
	else
		return F(x-y,y)+1;
}

//Q14
int F1(int ,int );
void Q14()
{
	int x,y;
	printf("Enter the  numbers: ");
	scanf(" %d %d",&x,&y);
	
	printf("%d",F1(x,y));
}

int F1(int M,int N)
{
	if (M==0 || M>=N>=1)
		return 1;
	else
		return F1(M-1,N)+F1(M-1,N-1);
}

//Q21&24
int swap_cv(int ,int );
int swap_cr(int *,int *);
void Q21_24()
{
	int m,n;
	printf("Enter the numbers: ");
	scanf(" %d %d",&m,&n);

	swap_cv(m,n);
	printf("%d,%d\n",m,n);
	swap_cr(&m,&n);
	printf("%d,%d\n",m,n);
}

int swap_cv(int x,int y)
{
	x=x+y;
	y=x-y;
	x=x-y;
}

int swap_cr(int *x,int *y)
{
	*x=*x+*y;
	*y=*x-*y;
	*x=*x-*y;
}

#include <math.h>
//Q22
float power(int ,int );
void Q22()
{
	int b,e;
	printf("Enter the values of base and expo: ");
	scanf(" %d %d",&b,&e);

	printf("%f",power(b,e));
}

float power(int x,int y)
{
    int i;
	int b=1;
	float B=1;
	if (y>=0)
	{
		for (i=0;i<y;i++)
			b*=x;
	}
	else
	{
		for (i=0;i<(-y);i++)
        {
			B/=(float)x;
            printf("%f ",B);
        }
    }

	if(y>=0)
		return b;
	else
		return B;
}
			
//Q23
float CI(int ,int ,int );
void Q23()
{

	int p,r,t;
	printf("Enter p,r,t: ");
	scanf(" %d %d %d",&p,&r,&t);

	printf("%f",CI(p,r,t));
}

float CI(int p,int r,int t)
{
	return (p*pow((1+(float)r/100),t)-p);
}

//Q25
int Fact(int );
int Fact_rev(int );
void Q25()
{
	int num;
	printf("Enter the number: ");
	scanf(" %d",&num);

	printf("%d",Fact(num));
	printf("\n%d",Fact_rev(num));
}

int Fact(int n)
{
	int i;
	int b=1;
	for (i=n;i>=1;i--)
		b*=i;

	return b;
}

int Fact_rev(int n)
{
	if (n==0)
		return 1;
	else
		return n*Fact_rev(n-1);
}

//Q27
int HCF(int ,int );
int HCF_rev(int ,int );
void Q27()
{
	int a,b;
	printf("Enter the numbers: ");
	scanf(" %d %d",&a,&b);

	printf("%d",HCF(a,b));
	printf("\n%d",HCF_rev(a,b));
}

int HCF(int m,int n)
{
	int res,res1;
	res=m%n; //10%6=4 6%4=2 4%2=0
	while (res)
	{
			res1=n%res;
			n=res;
			res=res1;
	}
	
	return n;
}

int HCF_rev(int m,int n)
{
	int res;
	res=m%n;

	if(!res)
		return n;
	else
		return HCF(n,res);
}


//Q28
float Pow(int ,int);
float Pow_rec(int ,int );
void Q28()
{
	int b,e;
	printf("Enter the base and expo: ");
	scanf(" %d %d",&b,&e);

	printf("%f",Pow(b,e));
	printf("\n%f",Pow(b,e));
}

float Pow(int x,int y)
{
	int b=1;
	int i;
	for (i=0;i<y;i++)
		b*=x;
	
	return b;
}

float Pow_rec(int x,int y)
{
	if (!y)
		return 1;
	else
		return x*Pow_rec(x,y-1);
}

//Q29
int Fib(int );
int Fib_rec(int );
void Q29()
{
	int n;
	printf("Enter the number till which seriesid to be found: ");
	scanf(" %d",&n);

	int i;
	for (i=0;i<=n;i++)
		printf("%d ",Fib(i));
	printf("\n");
	for (i=0;i<=n;i++)
		printf("%d ",Fib_rec(i));
}

int Fib(int i)
{
	static int p1=1,p2=0,res;
	if (i==0)
		return 0;
	else if (i==1)
		return 1;
	else 
	{
        //printf("%d,%d,%d\n",res,p1,p2);
		res=p1+p2;
		p2=p1;
		p1=res;
       // printf("%d,%d,%d\n",res,p1,p2);
	}
	return res;
}
		
int Fib_rec(int i)
{
	if (i==0)
		return 0;
	else if (i==1)
		return 1;
	else 
		return Fib_rec(i-1)+Fib_rec(i-2);
}
		
void main()
{
    Q29();
}

#include <stdio.h>
//Theory
#include <ctype.h>
void SE_2()
{
    char c;
    printf("Enter any char: \n");
    scanf("%c",&c);

    printf("%d\n",isalnum(c));
    printf("%d\n",isalpha(c));
    printf("%d\n",isdigit(c));
    printf("%d\n",islower(c));
    printf("%d\n",isupper(c));
    printf("\t%d\n",isspace(c));
    printf("\t%d\n",ispunct(c));
    printf("%d\n",isxdigit(c));
    printf("\t%d\n",isblank(c));
    printf("%d\n",isalpha(c));
    printf("%c\n",tolower(c));
    printf("%c\n",toupper(c));
}

void return_value_scanf()
{
    int a;char b;float c;
    printf("%d",scanf("%d %c %f",&a,&b,&c));    
}

void SE9()
{
    float sal;
    char G;
    printf("Enter ur salary and gender: ");
    scanf("%f %c",&sal,&G);

    if (sal<10000.0)
    {
        if ((G=='M')||(G=='m'))
            printf("%f",sal*1.07);
        else 
            printf("%f",sal*1.12);    
    }
    else
    {
        if ((G=='M')||(G=='m'))
            printf("%f",sal*1.05);
        else 
            printf("%f",sal*1.10);      
    }
}

#include <math.h>
void SE15()
{
    float a,b,c;
    printf("Enter the values of constants of QE: ");
    scanf("%f %f %f",&a,&b,&c);
    printf("%fx^2+%fx+%f",a,b,c);

    float D;
    D=pow(b,2)-4*a*c;
    printf("\n%f\n",D);

    float x1,x2,x;
    if (D>0)
    {
        x1=(-b-sqrt(D))/(2*a);
        x2=(-b+sqrt(D))/(2*a);
        printf("%f %f",x1,x2);
    }
}

#define eps 1e-5
void epsilon()
{
    float n1,n2;
    scanf("%f %f",&n1,&n2);

    printf("%f\n",n1/n2);
    if (fabs(n1/n2*n2-n1)<=eps)
        printf("Equal");
}

void dangling_if_else()
{
    int a=1,b=2,c=3;
   if(a==10)
    if(b==2)
        printf("b");
    else
        printf("not b");
    else if (c==3)
        printf("c");
    else
        printf("not a");
}

void SE17()
{
    char ch;
    scanf("%c",&ch);

    switch (ch)
    {
        case 'A':
        case 'a':
        case 'E':
        case 'e':
        case 'I':
        case 'i':
        case 'O':
        case 'o':
        case 'U':
        case 'u':
            printf ("Vowel\n");
            break;
        default:
            printf("Consonant");
    }
}

void SE23()
{
    int i=2;
    int n;
    scanf("%d",&n);

    int max=n;

    while(i<=5)
    {
        int num;
        scanf("%d",&num);

        max=max<num?num:max;

        i++;
    }

    printf("%d",max);
}

void SE27()
{
    int n;
    scanf("%d",&n);

    int i=1;
    do{
        printf("%d\t%d\n",i*i,i*i*i);
        i++;
    }
    while(i<=5);
}

void SE36()
{
    int n;
    scanf(" %d",&n);
    
    int i,j,c=0;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=i;j++)
            printf("%d",c++);
        printf("\n");
    }
}

void SE38()
{
    int n;
    scanf(" %d",&n);

    int i,j;
    int sp=n-1;
    for (i=1;i<=n;i++) //lines
    {
        for (j=sp;j>0;j--)
            printf("&");
        for (j=1;j<=i;j++)
            printf("%d",j);
        printf("\n");
        sp--;
    }
}

void SE39()
{
    int n;
    scanf("%d",&n);

    int i,j;
    int sp=n-1;

    for (i=1;i<=n;i++)
    {
        for (j=sp;j>0;j--)
            printf("&");
        for (j=1;j<=i;j++)
            printf("%d",j);
        for (j=i-1;j>=1;j--)
            printf("%d",j);
        for (j=sp;j>0;j--)
            printf("&");
        sp--;
        printf("\n");
    }
    
}

void SE46()
{
    int n;
    scanf(" %d",&n);
    int c=0,p=0;
    int flag;
    if (n!=-1)
    {    
        int num=n;
        do
        {
            int i;
            for (i=2;i<=(num/2);i++)
            {
                if (num%i==0)
                {
                    flag=0; //composite
                    break;
                }
                else    
                    flag=1; //prime
            }
            if (flag==0)
                c++;
            else
                p++;
            scanf(" %d",&num);
        }while(num!=-1);
    }
    printf("%d %d",c,p);
}

void SE48()
{
    int num;
    scanf(" %d",&num);

    int q=num;
    int nd=0;    
    while(q!=0)
    {
        q/=10;
        nd++;
    }
    
    int i;
    int d;
    q=num;
    int rev=0;
    for (i=nd;i>=1;i--)
    {
        d=q%10;
        q/=10;

        int b=1;
        int j;
        for (j=i-1;j>=1;j--)
            b*=10;
        rev+=d*b;
    }
    printf("%d",rev);
}

void SE50()
{
    //printf("%x\t%o\t",10,10);
    int num;
    scanf(" %d",&num);

    int i=0;
    int q=num;
    int bin=0;
    int d;
    int b=1;
    while(q!=0)
    {
        d=q%2;
        printf("%d\n",d);
        q/=2;
        
        bin+=d*b;
        printf("%d\n",bin);
        b*=10;
    }
    printf("%d\n",bin);
    /*
    for (i=0;i<5;i++)
        printf("%d\t",pow(10,i));
    */
    //printf("\n%f\n",pow(10,0)*1);

}

void SE51()
{
    int num;
    scanf(" %d",&num);

    int oct=0,i=0;
    int b,d;
    int q=num;
    while(q!=0)
    {
        d=q%8;
        q/=8;

        b=pow(10,i);
        oct+=d*b;
        i++;
    }
    printf("%d",oct);
}

void SE52()
{
    int num;
    printf("Enter the binary number: ");
    scanf(" %d",&num);

    //int q=num;
    int deci=0;
    int i=0;
    int d,b=1;
    while(num!=0)
    {
        d=num%10;
        num/=10;

        //b=pow(2,i);
        deci+=d*b;
        //i++;
        b*=2;
    }
    printf("%d",deci);
}

void SE53()
{
    int num;
    printf("Enter the octal number: ");
    scanf(" %d",&num);

    int deci=0;
    int d,b=1;
    while(num!=0)
    {
        d=num%10;
        num/=10;

        deci+=d*b;
        b*=8;
    }
    printf("%d",deci);
}

void SE55()
{
    int a,b,temp;
    scanf(" %d %d",&a,&b);

    while(b)
    {
        temp=b;
        b=a%b;
        a=temp;
    }
    printf("%d",a);
}

void SE57()
{
    int n;
    scanf(" %d",&n);

    int i;
    float sm=0,t;
    for (i=1;i<=n;i++)
    {
        sm+=1/(float)(i*i);
        //printf("%f\n",t);
        sm+=t;
    }
    printf("%f",sm);
}

void SE58()
{
    int n;
    scanf(" %d",&n);

    float sm=0;
    int i;
    for (i=1;i<=n;i++)
        sm+=i/((float)(i+1));
    printf("%f",sm);
}

void SE59()
{
    int n;
    scanf(" %d",&n);

    int i;
    float sm=0;
    for (i=1;i<=n;i++)
        sm+=pow(i,i)/i;
    printf("%f",sm);
}

void SE62()
{
    int num;
    scanf(" %d",&num);

    int q=num;
    int nd=0;
    while (q!=0)
    {
       q/=10;
       nd++;
    }
    
    int d,i,j;
    q=num;
    int sm=0;
    for (i=1;i<=nd;i++)
    {
        int b=1;
        d=q%10;
        q/=10;

        for (j=1;j<=nd;j++)
        {
            b*=d;
            printf("%d\n",b);
        }
        sm+=b;
        printf("%d\n",sm);
    }
    if (num==sm)
        printf("Armstrong");
    else
        printf("No armstrong");
}

void SE64()
{
    int day,days;
    scanf("%d %d",&day,&days);

    printf("S M T W T F S\n");

    //space
    int i;
    for (i=1;i<=2*(day-1);i++)
        printf(" ");
    //numbers
    for (i=1;i<=days;i++)
    {
        printf("%d ",i);
        if ((i+(day-1))%7==0)
            printf("\n");
    }
}

void main()
{
    SE_2();

    /*
    int a,b;
    a=b=100000;
    printf("\n%ld\n",a*b);
    printf("%d %d",sizeof("%ld"),sizeof("%f"));
    */
   /*
   int a;
   a=pow(10,2);
   printf("%d",3*a);
   */

  /*
  int num=10;
  for(num++;num<=100;num=100)
    printf("%d\n",num);
    */
}
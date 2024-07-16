#include <stdio.h>
//Output Qns
void Q3()
{
    int a;
    a=15/10.0 +3/2;
    printf("\n%d",a);
}

void Q8()
{
    int a=4,b=12,c=-3;
    int res;
    res=(a/2.0==0.0&&b/2.0!=0.0)||c<0.0;
    printf("%d",res);
}

void Q10()
{
    int a,b;
    printf("\n a=%d\t b=%d\ta+b=%d",a,b,a+b);
}

void Q15()
{
    int a=2,b=3,c,d;
    c=a++;
    a+=1;
    d=++b;
    printf("%d\t%d\t%d",c,d,a);
}

void Q16()
{
    int _A=30;
    printf("%d",_A);
}

void Q17()
{
    int a=2,b=4;
    a++;
    ++b;
    printf("%d\t%d",a,b);
}

void Q18_Q19()
{
    int a=4,b=5;
    //printf("%d",++(a-b));
    printf("%d",++a-b);
}

void Q21_Q23()
{
    int a=2;
    a=a+3*a++;
    printf("%d\n",a);
    printf("%d\t%d\t%d",a++,a,++a);
}

void Q22()
{
    int res;
    res=3+5-1*17%-13;
    printf("%d",res);
    printf("%d",17%-13);
}

void Q26()
{ 
    char str[]="Welcome to C programming";
    printf("\n %40.14s",str);
}

void Q28()
{
    int a;
    float b;
    scanf("%2d",&a);
    scanf(" %f",&b);
    printf("%d\t%f",a,b);
}

void Q29()
{
    char a,b,c;
    scanf("%c %c %c",&a,&b,&c);
    a++;
    b++; c++;
    printf("%c %c %c",a,b,c);
}
void main()
{
    Q16();
}
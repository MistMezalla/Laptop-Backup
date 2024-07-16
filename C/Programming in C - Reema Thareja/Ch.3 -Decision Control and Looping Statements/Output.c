#include <stdio.h>

void Q1()
{
    int a=2,b=3,c=4;
    if(c!=100)
        a=10;
    else
        b=10;
        if (a+b>10)
        c=12;
        a=20;
        b=++c;
    printf("%d,%d,%d",a,b,c);
}

void Q2to6()
{
    int a=2,b=3,c=4;
    if(a == 0 || b>=c && c>0)
    if (a&&b)
        c=10;
    else if (a)
        c=20;
    else 
        c=30;
    printf("%d,%d,%d",a,b,c);
}

void Q7to8()
{
    int a=2,b=3,c=4;
    if (a=b<c)
    {
        c++;
        a--;
    }
    b++;
    printf("%d,%d,%d",a,b,c);
}

void Q9()
{
    switch (/*ch*/ 65)
    {
        case 'a':
        case 'A':
            printf("\nA");
            break;
        default:
            printf("Get Lost");
    }
}

void Q15()
{
    int a=10,b=20,c=30,d=40;
    if (c>d)
    if(c<b)
        printf("\nc");
    else if (a<c)
        printf("\na");
    if (a>b)
        printf("\nb");
    else 
        printf("\nd");
}

void Q16()
{
    char ch='Y';
    switch (ch)
    {
        default:
            printf("\n Yes or NO");
        case 'Y':
            printf("Yes");
            break;
        case 'N':
        printf("No");
        break;
    }
}

void Q17()
{
    int num=10;
    for (num++;num;num++)
        printf("%d\t",num);
}

void Q18to19()
{
    int num=10;
    for(;!num;)
        printf("%d\t",num);
}

void Q22()
{
   int i=0;
   do
    {
        printf("%d",i);
        i++;
    }
    while(i<=0);
}

void Q26()
{
    int x=-1;
    unsigned int y=1;
    if(x<y)
        printf("Hello");
    else    
        printf("Hi");
    printf("%d,%d",x,y);
}

void Q27()
{
    char ch=-63;
    int num=-36;
    unsigned int unum= -18;

    if (ch>num)
    {
        printf("A");
        if (ch>num)
            printf("B");
        else
            printf("C");
    } 
    else
    {
        printf("D");
        if(num<unum)
            printf("E");
        else 
            printf("F");
    }
}

void Q28to30()
{
    int num=10;
    for(num++;num<=11;num=0)
        printf("%d\t",num);
}

void Q33()
{
    int i=0;
    do
    {
        if(i>10)
        {
        printf("Hi\n");
        continue;
        }
        i++;
    } while (i<20);
    printf("%d\t",i);
    
}

void Q34to35()
{
    int i,j;
    for (i=10;i>0;i--)
    {
        printf("\n");
        for(j=i;j>=0;j--)
        printf("%d",j);
    }
}

void main()
{
    Q28to30();
    
    printf("\n");
    int i,j;
    for(i=1,j=0;i+j<=10;i++)
    {
        printf("%d",i);
        j+=2;
    }
    
}
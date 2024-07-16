#include <stdio.h>
#include <math.h>
//Programming Exercise

void Q1()
{
    int n;
    float m;

    printf("Enter the float value: ");
    scanf(" %f",&m);

    if (m>3.14)
        printf("%f",m+10);
}

void Q2_M1()
{
    int n;
    printf("Enter the value of number: ");
    scanf(" %d",&n);
    
    int m=n/2+1;
    int factors[m];

    int i,ind=0;
    for (i=1;i<=m;i++)
    {
        if (n%i==0)
        {
            factors[ind]=i;
            ind++;
        }
    }

    int num,j,k=0;
    int prime_fac[ind];
    for (i=0;i<ind;i++)
    {
        int flag=0; //Prime
        //printf("Hello\t");
        num=factors[i];
        if (num==1)
            continue;
        else 
        {
            for (j=2;j<=(num/2+1);j++)
            {
                //printf("hi\t");
                if(num%j==0)
                {
                    //printf("Wow\t");
                    flag=1; //Composite
                    break;
                }
            }
            //printf("%d\n",flag);
            if (flag==0)
            {
                //printf("Bye\t");
                prime_fac[k]=num;
                k++;
                //printf("%d\n",prime_fac[k]);
            }
        }
    }

    for (i=0;i<k;i++)
        printf("%d ",prime_fac[i]);
}

int isPrime(int num);

void Q2_M2()
{
    int n;
    printf("Enter the value of number: ");
    scanf(" %d",&n);
    
    int m=n/2+1;
    int factors[m];

    int i,ind=0;
    for (i=1;i<=m;i++)
    {
        if (n%i==0)
        {
            factors[ind]=i;
            ind++;
        }
    }

    int prime_fac[ind];
    int k=0;
    for (i=0;i<ind;i++)
    {    
        if (isPrime(factors[i]))
        {
            prime_fac[k]=factors[i];
            k++;
        }
    }
    for (i=0;i<k;i++)
        printf("%d ",prime_fac[i]);
}

int isPrime(int x)
{
    int i;
    int flag=1; //prime

    if (x==1)
        return 0;
    else
    {
        for (i=2;i<=(x/2+1);i++)
        {
            if (x%i==0)
            {
                return 0;
            }
        }
    }
    return 1;
}


void Q4()
{
    int l;
    printf("Number of lines: ");
    scanf(" %d",&l);

    int i,j;
    int c=1;
    for (i=1;i<=l;i++)
    {
        for (j=1;j<=i;j++)
        {
            printf("%d",c);
            c++;
        }
        printf("\n");
    }
}
/*
void Q6()
{
    int n;
    printf("Enter the choice no: ");
    scanf(" %d",&n);

    switch (n)
    {
        case 1:
            int i;
            int num[3];
            for (i=0;i<3;i++)
            {
                printf("Enter the number: ");
                scanf(" %d",&num[i]);
            }
            break;


    
    }
}
*/
void Q7()
{
    int angle;
    printf("Enter the angle in degrees and in multiple of 15: ");
    scanf(" %d",&angle);

    float x;
    x=angle*3.14/180;
    printf("%f",sin(x));
}

void Q10()
{
    int  ang;
    printf("Enter the angle in degrees: ");
    scanf(" %d",&ang);

    float x;
    x=ang%360;

    if(x>0 && x<90)
        printf("1st Quad");
    else if(x>90 && x<180)
        printf("2nd Quad");
    else if(x>180 && x<270)
        printf("3rd Quad");
    else if(x>270 && x<360)
        printf("4th Quad");
}

void Q16()
{
    float time;
    char vehicle;

    printf("Enter the type of vehicle:-\nCar=C\nTruck=t\nBus=b\nScooter=s\nMoter Cycle=m\nCycle=c\n: ");
    scanf(" %c",&vehicle);

    printf("Time in hrs: ");
    scanf(" %f",&time);

    switch(vehicle)
    {
        case 't':
        case 'b':
            printf("%f",time*20);
            break;
        case 'C':
            printf("%f",time*10);
            break;
        case 'm':
        case 'c':
        case 's':
            printf("%f",time*5);
            break;
    }

}

void Q20()
{
    int n;
    printf("Enter the number.\nEnter 999 to stop: ");
    scanf(" %d",&n);

    if (n==999)
        return;
    else
    {
        int r;
        int b=1;
        int bin=0;

        if (n>0)
        {
            while(n)
            {
                r=n%2;
                n/=2;

                bin+=r*b;
                b*=10;
            }
        }
        printf("%d",bin);
    }
}

void Q23()
{
    int l;
    printf("Enter the number of lines: ");
    scanf(" %d",&l);

    int i,j;
    for(i=1;i<=l;i++)
    {
        if (i==1 || i==l)
        {
            for (j=1;j<=l;j++)
                printf("*");
            printf("\n");
        }
        else
        {
            for (j=1;j<=l;j++)
            {
                if (j==1 || j==l)
                    printf("*");
                else
                    printf(" ");
            }
            printf("\n");
        }
    }
}

void Q24()
{
    int l;
    printf("Enter the number of lines: ");
    scanf(" %d",&l);

    int i,j;
    for (i=1;i<=l;i++)
    {
        if (i==1)
        {
            for (j=1;j<=l;j++)
            {
                if (j==i)
                    printf("$");
                else 
                    printf("*");
            }
            printf("\n");
        }

        else if (i==l)
        {
            for (j=1;j<=l;j++)
            {
                if (j==i)
                    printf("$");
                else
                    printf("*");
            }
            printf("\n");
        }

        else
        {
            for (j=1;j<=l;j++)
            {
                if (j==i)
                    printf("$");
                else if (j==1 || j==l)
                    printf("*");
                else
                    printf(" ");
            }
            printf("\n");
        }
    }
}

void Q25()
{
    int l;
    printf("Enter the number of lines: ");
    scanf(" %d",&l);

    int i,j;
    for (i=1;i<=l;i++)
    {
        if (i==1 || i==l)
        {
            for (j=1;j<=l;j++)
            {
                if (j==i || j==(l-i+1))
                    printf("$");
                else
                    printf("*");
            }
            printf("\n");
        }
        else
        {
            for (j=1;j<=l;j++)
            {
                if (j==i || j==(l-i+1))
                    printf("$");
                else if (j==1 || j==l)
                    printf("*");
                else
                    printf(" ");
            }
            printf("\n");
        }
    }
}

void Q28_1()
{
    int n;
    printf("Enter the value of n: ");
    scanf (" %d",&n);
    
    int num;
    printf("Enter the number: ");
    scanf(" %d",&num);

    int i;
    int sum=0;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        {
            sum+=(int)pow(num,i);
            printf("%d\t",(int)pow((float)num,(float)i));
        }
        else
        {
            sum-=(int)pow(num,i);
            printf("%d\t",(int)pow(num,i));
        }
    }
    printf("\n%d",sum);
}

void Q31()
{
    int n;
    printf("Enter the number: ");
    scanf (" %d",&n);

    int q;
    q=n;
    int nd=0;
    while (q)
    {
        q/=10;
        nd++;
    }

    int arr[nd];
    q=n;
    int i;
    for (i=nd-1;i>=0;i--)
    {
        arr[i]=q%10;
        q/=10;
    }

    int a=nd,b=1,sp=5;
    int j;
    for (i=0;i<nd;i++)
    {
        for (j=0;j<a;j++)
            printf("%d",arr[j]);
        for (j=0;j<sp;j++)
            printf(" ");
        for (j=0;j<b;j++)
            printf("%d",arr[j]);
        printf("\n");
        a--;
        sp++;
        b++;
    }
}

void main()
{
    Q31();
}
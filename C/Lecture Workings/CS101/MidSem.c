#include <stdio.h>
int isPrime(int n);
int factorial(int n);
int even_odd(int n)
{
    int q=n;
    int nd=0;
    while (q!=0)
    {
        q/=10;
        nd++;
    }
    //printf("%d\n",nd);
    
    int num[nd];
    int ind=0;
    q=n;
    while (q!=0)
    {
        num[ind]=q%10;
        ind++;
        q/=10;
    }
    /*
    int j;
    for (j=0;j<nd;j++)
        printf("%d\t",num[j]);
    */

    
    int o,e; //size of odd and even arrays
    int i;
    if (nd%2!=0)
    {
        o=(nd+1)/2;
        e=(nd-1)/2;
    }
    else
    {
        o=(nd)/2;
        e=(nd)/2;
    }
    int odd[o];
    int even[e];

        int co=0,ce=0; //Index counters for odd and even
        for (i=0;i<nd;i++)
        {
            if(i%2==0)
            {
                odd[co]=num[i];
                co++;
            }
            else
            {
                even[ce]=num[i];
                ce++;
            }
        }


    printf("The digit at odd places are: ");
    for (i=o-1;i>=0;i--)
        printf("%d ",odd[i]);
    
    printf("\n");

    printf("The digit at even places are: ");
    for (i=e-1;i>=0;i--)
        printf("%d ",even[i]);

    int odd_num=0,even_num=0;
    int b=1;
    // odd num 
    for (i=0;i<o;i++)
    {
        odd_num+=odd[i]*b;
        b*=10;
    }
    
    // even num
    b=1;
    for (i=0;i<e;i++)
    {
        even_num+=even[i]*b;
        b*=10;
    }
    
    printf("\n%d %d",odd_num,even_num);
    
    int m=odd_num;
    int factors[m];
    int cf=0;
    //printf("\n%d",m);
    printf("\nFactors of %d are: ",m);
    for (i=1;i<=(m+1)/2;i++)
    {
        if (m%i==0)
        {
            printf("%d ",i);
            factors[cf]=i;
            cf++;
        }
    }
    
    int sum_ef=0;
    for(i=0;i<e;i++)
    {
        sum_ef=sum_ef+factorial(even[i]);
        //printf("%d\t",factorial(even[i]));
    }
    printf("\nSum of factorails at even places: %d",sum_ef);
    
    
    int flag;
    
    printf("\nPrime factors of %d: ",m);
    for (i=0;i<cf;i++)
    {
        flag=isPrime(factors[i]);

        if (flag==0)
            printf("%d ",factors[i]);
    }

    printf("\nNon Prime factors of %d: ",m);
    for (i=0;i<cf;i++)
    {
        flag=isPrime(factors[i]);
        if (flag==1)
            printf("%d ",factors[i]);
    }
        
    
}

int factorial(int n)
{
    int fact=1;
    int i;
    if (n==0)
        fact=1;
    else
        for(i=1;i<=n;i++)
        {    
            fact*=i;
            printf("%d \t",fact);
        }
}

int isPrime(int n)
{
    int i;
    int flag;
    
    if (n==1)
        return 1;

    else    
    {
        for (i=2;i<=(n+1)/2;i++)
        {
            if(n%i==0)
            {
                flag=1; //non prime
                break;
            }
            else
                flag=0; //Prime
        }
    }
    if (flag==0)
        return 0;
    else
        return 1;
}

void main()
{
    int num;
    printf("Enter the number: ");
    scanf(" %d",&num);
    even_odd(num);
}
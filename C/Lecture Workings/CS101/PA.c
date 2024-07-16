#include <stdio.h>
void PA4_Q1()
{
    /*
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);
    */
    int j,sum=0;
    for (j=1;j<=500;j++)
    {
        int nd=0;
        int q=j;
        while(q!=0)
        {
            q/=10;
            nd+=1;
        }
    
        int i,d,sm=0;
    
        q=j;
        while(q!=0)
        {
            int b=1;
            d=q%10;
            q/=10;

            for (i=1;i<=nd;i++)
                b*=d;
            sm+=b;
        }
        if (j==sm)
        {
            printf("%d\n",j);
            sum+=j;
        }
        /*
        else
            printf("Not armstrong");
        */
    }
    printf("%d",sum);
}

void PA4_Q2()
{
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);

   int q=num,nd=0,flag;
   while(q!=0)
   {
        q/=10;
        nd+=1;
   }
   
    if (nd%2==0)
    {
        int i,j,l=nd,nf=num,nr=num,df,dr;
        for (i=nd/2;i>=1;i--)
        {
            int b=1;
            for(j=1;j<=l-1;j++)
                b*=10;
            
            df=nf/b;
            nf%=b;

            dr=nr%10;
            nr/=10;
            l-=1;

            if(df==dr)
                flag=1;
            else
            {
                flag=0;
                break;
            }
        }
    }
    else
    {
        int i,j,l=nd,nf=num,nr=num,df,dr;
        for (i=(nd-1)/2;i>=1;i--)
        {
            int b=1;
            for(j=1;j<=l-1;j++)
                b*=10;
            
            df=nf/b;
            nf%=b;

            dr=nr%10;
            nr/=10;
            l-=1;
            
            if(df==dr)
                flag=1;
            else
                flag=0;
                break;
        }
    }
    if (flag==1)
        printf("Palindrome");
    else
        printf("Not palindrome");
}

void PA5_Q1g()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    //Upper Tri
    int i,spu=(l-1)/2;
    for (i=1;i<=(l+1)/2;i++)
    {
        int a,b,c;
        
        for (c=spu;c>0;c--)
            printf("&");
        spu--;
        for (a=1;a<=i;a++)
                printf("%d",a);
        for (b=i-1;b>=1;b--)
                printf("%d",b);
        printf("\n");
    }
    //Lower Tri
    int spd=1;
    for (i=(l-1)/2;i>=1;i--)
    {
        int a,b,c;

        for (c=1;c<=spd;c++)
            printf("&");
        spd++;
        for (a=1;a<=i;a++)
                printf("%d",a);
        for (b=i-1;b>=1;b--)
                printf("%d",b);
        printf("\n");
    }
}

void PA5_Q1h()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    //Upper Tri
    int i,j;
    for (i=1;i<=(l+1)/2;i++)
    {
        if(i%2==0) //even line
        {
            for (j=1;j<=2*i-1;j++)
            {
                if (j%2==0)
                    printf("1");
                else
                    printf("0");
            }
            printf("\n");
        }
        else
        {
            for (j=1;j<=2*i-1;j++)
            {
                if (j%2==0)
                    printf("0");
                else
                    printf("1");
            }
            printf("\n");
        }
    }
    //Lower Tri
    
    for (i=(l-1)/2;i>=1;i--)
    {
        if(i%2!=0) //odd line
        {
            for (j=1;j<=2*i-1;j++)
            {
                if (j%2!=0)
                    printf("1");
                else
                    printf("0");
            }
            printf("\n");
        }
        else
        {
            for (j=1;j<=2*i-1;j++)
            {
                if (j%2!=0)
                    printf("0");
                else
                    printf("1");
            }
            printf("\n");
        }
    }
}

void PA5_Q1c()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    
    int i,j;
    for (i=1;i<=l+2;i++)
    {
        int p=0,n=1,num;
        for(j=3;j<=i;j++)
        {
            if (i==1)
                printf("%d\n",p);
            else if(i==2)
                printf("%d\n",n);
            else
            {
                //for(j=3;j<=i;j++)
                num=n+p;
                p=n;
                n=num;
                printf("%d",num);
                //printf("") //0 1 1 2 3 5 8 13
            }   
        }    
        printf("\n");
    }



}
void main()
{
    PA5_Q1c();
}
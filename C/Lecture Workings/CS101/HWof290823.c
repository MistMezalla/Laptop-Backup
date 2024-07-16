#include <stdio.h>

// HW of 29/08/23

void Q1()
{
    int row;
    
    printf("Enter the number of rows: ");
    scanf("%d",&row);

    int i,j;
    for (i=1;i<=row;i++) // For number of lines.
        {
            for (j=1;j<=i;j++)       // For stars.
                printf("*");
        printf("\n");
        }
}

void Q2()
{
    int row;
    printf("Enter the number of lines to be printed: ");
    scanf("%d",&row);

    int i,j;
    for (i=1;i<=row;i++) //For number of lines
    {
        for (j=1;j<=i;j++)
            printf("%d",j);
        printf("\n");
    }
}

void Q3()
{
   int lines;
   printf("enter the number of lines: ");
   scanf("%d",&lines);

   if (lines<=26)
   {
        int i,j;
        
        for (i=1;i<=lines;i++) //no of lines
        {   
            char k='A';
            for (j=1;j<=i;j+=1)
                {
                        printf("%c",k);
                        k+=1;
                }
            printf("\n");
        }
   }
   else
        printf("Enter a value less than 26");
}

void Q4a()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    int i,sl,sr,st,j=1;
    for (i=l;i>=1;i--) //No of lines.
    {
        for (sl=2*i-2;sl>=i;sl--)
            printf("&");
        for (st=1;st<=j;st+=1)
            printf("*");
        for (sr=2*i-2;sr>=i;sr--)
            printf("&");
    printf("\n");
    j+=2;
    }
}   
void Q4b()
{

}

void Q5()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    int i,j;
    for (i=1;i<=l;i++)
        {
            for (j=i;j>=1;j--)
                printf("%d ",j*j);
            printf("\n");
        }
}

void Q6a()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    int i,sl,p,sr;
    int j=0,k=1;
    for (i=l;i>=1;i--)
    {
        if (i%2==0)
        {
            for (sl=0;sl<=j-1;j++)
                printf("&");
            for (p=2*i-1;p>=1;p--)
                printf("*");
            /*
            for (sr=0;sr<=j-1;j++)
                printf("&");
            */
            printf("\n");
            j+=2;
        }
        /*
        else 
        {
            for (sl=1;sl<=k-1;k++)
                printf("&");
            for (p=2*l-1;p>=1;p--)
                printf("1");
            for (sr=1;sr<=k-1;k++)
                printf("&");
            printf("\n");
            k+=2;
        }
*/
    }
}

void Q6b()
{
    int l;
    printf("Enter the number of the lines: ");
    scanf("%d",&l);

    int i,sl,sr,p;
    int j=0,k=1;
    for (i=l;i>=1;i--)
    {
        if (i%2==0)
        {
            for (sl=1;sl<=j;sl++)
                printf("&");
            for (p=2*i-1;p>=1;p--)
                printf("*");
            for (sr=1;sr<=j;sr++)
                printf("&");
            printf("\n");
            j+=2;
        }
        else
        {
            for (sl=1;sl<=k;sl++)
                printf("&");
            for (p=2*i-1;p>=1;p--)
                printf("1");
            for (sr=1;sr<=k;sr++)
                printf("&");
            printf("\n");
            k+=2;
        }
    }
}

void trial()
{
    int i,j,k=1;
    for (i=1;i<=k;i++)
        printf("hi");
}

void Q7()
{
    int l;
    printf("Enter the number of lines: ");
    scanf("%d",&l);

    int i,j,pl,pr,sp;
    int k=1;

    for (j=2*l-1;j>=1;j--)
        printf("*");
    printf("\n");
    
    for (i=l;i>=1;i--)
    {
        for (pl=1;pl<=i-1;pl++)
            printf("*");
        for (sp=1;sp<=k;sp++)
            printf(" ");
        for (pr=1;pr<=i-1;pr++)
            printf("*");
    printf("\n");
    k+=2;
    }
}
void main()
{
    Q3();
}
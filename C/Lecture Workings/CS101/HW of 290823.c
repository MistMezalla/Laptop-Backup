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
   scanf("%d",lines);

   if (lines<=26)
   {
        int i,j;
        char k=65;
        for (i=1;i<=lines;i++) //no of lines
        {
            for (j=1;j<=lines;j+=1)
                {
                    printf("%c",k);
                    printf(k+=1);  
                }
            printf("\n");
        }
   }
   else
        printf("Enter a value less than 26");
}

void main()
{
    Q3();
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


//Q12
int Prime_composite(int *n)
{
    int i,flag=1;
    if (*n == 1 || *n==0)
        return 2;
    else
    {
        for (i=2;i<(fabs(*n))/2;i++)
        {
            if (*n%i==0)
                return 0;
        }
    }
    if (flag)
        return 1;
}

void Q12()
{
    int n,i;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int *parr=(int *)calloc(n,sizeof(int));
    
    printf("Enter the elements of the array: ");
    for (i=0;i<n;i++)
        scanf(" %d",parr+i);

    for (i=0;i<n;i++)
        printf("%d ",*(parr+i));
    printf("\n");

    for (i=0;i<n;i++)
    {
        if(Prime_composite(parr+i)==1)
            printf("%d is prime.\n",*(parr+i));
        else if (Prime_composite(parr+i)==2)
            printf("%d is neither prime nor composite.\n",*(parr+i));
        else
            printf("%d is composite",*(parr+i));
    }

        
}

//Q19
void str_find(char *pstr,char *pstr_sub)
{
    int n=strlen(pstr);
    int m=strlen(pstr_sub);

    int i,j=0;
    for (i=0;i<n;i++)
    {
        if(pstr[i]==pstr_sub[j])
        {
            do
            {
                printf("%c",pstr[i]);
                i++,j++;
            }while(pstr[i]==pstr_sub[j]);
        }
    }
}
void Q19()
{
    char str[100]="Oxford University Press";
    char *pstr=str;

    char str_sub[100]="University";
    char *pstr_sub=str_sub;
    str_find(pstr,pstr_sub);
}

void main()
{
    Q19();
}
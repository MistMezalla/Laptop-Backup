#include <stdio.h>
#include <string.h>

void shift(int n,char str[n+1],int pos,int amt)
{
    int i;
    for (i=n;i>=pos;i--)
    {
        str[i+amt]=str[i];
    }
}

void Q15()
{
    char st[20] = "Sipo";
    printf("Enter the string: ");
    //scanf(" %s",st);

    int l=strlen(st);
    int i;
    for (i=0;i<l;i+=2)
    {
        shift(l,st,i,1);
        st[i+1]=st[i];
    }
    printf("Updated string: %s",st);
    
}

void main()
{
    Q15();
}
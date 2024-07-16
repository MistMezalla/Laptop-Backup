#include <stdio.h>
#include <string.h>
#include<ctype.h>

#define MAX 100
#define EXP 100
int top=-1;
char st[MAX][EXP];

void push(char st[][EXP], char val)
{
    if(top==MAX-1)
    {
        printf("Stack Overflow\n");
        return;
    }
    else
    {
        top++;
        st[top][0]=val;
        st[top][1]='\0';
    }
}

char *pop(char st[][EXP])
{
    if(top==-1)
    {
        printf("Stack Underflow\n");
    }
    else 
    {
        top--;
        return(st[top+1]);
    }
}

void eval(char v1[],char v2[],char st[][EXP],char op)
{
    top++;
    int i=0,j=0;;
    while(v1[j]!='\0')
    {
        st[top][i]=v1[j];
        i++,j++;
    }
    st[top][i]=op;
    i++;
    j=0;
    while(v2[j]!='\0')
    {
        st[top][i]=v2[j];
        i++,j++;
    }
    st[top][i]='\0';
}

void postfix_infix(char s[],char d[])
{
    int i=0;
    while(s[i]!='\0')
    {
        if(isalnum(s[i]))
        {
            push(st,s[i]);
            i++;
            //printf("Hi");
        }
        else if(s[i]=='/' || s[i]=='*' || s[i]=='%' || s[i]=='+' || s[i]=='-')
        {
            //printf("Bye");
            char val1[MAX],val2[MAX];
            strcpy(val2,pop(st));
            strcpy(val1,pop(st));
            //printf("\n%s\t%s\n",val1,val2);
            eval(val1,val2,st,s[i]);
            //printf("%s",st[top]);
            i++;
        }
    }
    strcpy(d,pop(st));
}

void main()
{
    char postfix[100],infix[100];
    printf("Enter the postfix expression: ");
    scanf(" %[^\n]s",postfix);

    postfix_infix(postfix,infix);
    printf("The infix expression is: %s",infix);
}

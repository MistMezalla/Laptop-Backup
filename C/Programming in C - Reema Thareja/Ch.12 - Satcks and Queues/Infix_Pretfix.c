#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100
int top=-1;
char st[MAX];

void push(char st[],char val)
{
    if(top==MAX-1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        top++;
        st[top]=val;
    }
}

char pop(char st[])
{
    if (top==-1)
    {
        printf("Stack Underflow\n");
    }
    else 
    {
        top--;
        return (st[top+1]);
    }
}

int op_priority(char op)
{
    if(op == '/' || op == '*' || op == '%')
    return 1;
    else if(op == '+' || op == '-')
    return 0;
}

void infix_postfix(char s[],char d[])
{
    int i=0,j=0;
    while(s[i]!='\0')
    {
        if(s[i]=='(')
        {
            push(st,s[i]);
            i++;
        }
        else if(isalnum(s[i]))
        {
            d[j]=s[i];
            j++;
            i++;
        }
        else if(s[i]=='/' || s[i]=='*' || s[i]=='%' || s[i]=='+' || s[i]=='-')
        {
            while(st[top]!='(' && top!=-1 && op_priority(st[top])>op_priority(s[i]))
            {
                d[j]=pop(st);
                j++;
            }
            push(st,s[i]);
            i++;
        }
        else if(s[i]==')')
        {
            while(st[top]!='(' && top!=-1)
            {
                d[j]=pop(st);
                j++;
            }
            if(top==-1)
            {
                printf("Wrong expresssion\n");
                return;
            }
            pop(st);
            i++;
        }
        else
        {
            printf("Wromg exp\n");
        }
    }
    
    while(st[top]!='(' && top!=-1)
    {
         d[j]=pop(st);
                j++;
    }
    d[j]='\0';
}

void rev(char s[])
{
    int l=strlen(s);
    char d[MAX];
    int i;
    int j=0;
    for (i=l-1;i>=0;i--)
    {
        if(s[i]=='(')
        {
            d[j]=')';
            j++;
        }
        else if(s[i]==')')
        {
            d[j]='(';
            j++;
        }
        else
        {
            d[j]=s[i];
            j++;
        }
    }
    d[j]='\0';
    strcpy(s,d);
}

void infix_prefix(char s[],char t[])
{
    rev(s);
    infix_postfix(s,t);
    rev(t);
}

void main()
{
    char infix[100],prefix[100];
    printf("Enter the infix expression: ");
    scanf(" %[^\n]s",infix);

    infix_prefix(infix,prefix);
    printf("The prefix exp is %s",prefix);
}
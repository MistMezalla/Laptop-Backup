#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 100
int top=-1;
char st[SIZE];

void push(char st[],char ch)
{
    if(top==SIZE-1)
    {
        printf("Stack overflow\n");
        return;
    }
    top++;
    st[top]=ch;
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

int op_pr(char op)
{
    if (op=='/' || op=='*' || op=='%')
        return 1;
    else if(op=='+' || op=='-')
        return 0;
}

void infix_postfix(char s[],char d[])
{
    int i=0,j=0;
    while(s[i]!='\0')
    {
        if(isalnum(s[i]))
        {
            d[j]=s[i];
            i++;
            j++;
        }
        else if(s[i]=='(')
        {
            push(st,s[i]);
            i++;
        }
        else if(s[i]=='+' || s[i]=='-' || s[i]=='*' || s[i]=='/' || s[i]=='%')
        {
            while(st[top]!='(' && top!=-1 && (op_pr(s[i])>op_pr(st[top])))
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
            if (top==-1)
            {
                printf("Inc Exp\n");
            }
            pop(st);
            i++;
        }
        else 
        {
            printf("Inc Exp\n");
        }
    }
    while(top!=-1 && st[top]!='(')
    {
        d[j]=pop(st);
        j++;
    }
    d[j]='\0';
}

void main()
{
    char postfix[100],infix[100];
    printf("Enter the infix exp: ");
    scanf(" %[^\n]s",infix);

    infix_postfix(infix,postfix);
    printf("The postfix expression is: %s",postfix);
}

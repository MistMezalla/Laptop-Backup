#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

int top=-1;
char st[MAX];

void Push(char st[],char val)
{
    if (top==MAX-1)
    {
        printf("Stack overflow\n");
        return;
    }

    top++;
    st[top]=val;
}

char Pop(char st[])
{
    if (top==-1)
    {
        printf("Stack underflow\n");
    }

    else 
    {
        top--;
        return(st[top+1]);
    }
    
}

int op_priority(char op)
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
        if (s[i]=='(')
        {
            Push(st,s[i]);
            i++;
        }
        else if(isalnum(s[i]))
        {
            d[j]=s[i];
            i++,
            j++;
        }
        else if(s[i]=='/' || s[i]=='*' || s[i]=='%' || s[i]=='+' || s[i]=='-')
        {
            while(st[top]!='(' && top!=-1 && (op_priority(st[top])>op_priority(s[i])))
            {
                d[j]=Pop(st);
                j++;
            }
            Push(st,s[i]);
            i++;
        }
        else if(s[i]==')')
        {
            while(top!=-1 && st[top]!='(')
            {
                d[j]=Pop(st);
                j++;
            }
            if(top==-1)
            {
                printf("Incorrect Expression\n");
                return;
            }
            Pop(st);
            i++;
        }
        else
        {
            printf("Incorrect Expression\n");
                return;
        }
    }
    while(st[top]!='(' && top!=-1)
    {
        d[j]=Pop(st);
        j++;
    }
    d[j]='\0';
}

void main()
{
    char infix[100],postfix[100];
    printf("Enter the infix expression: ");
    scanf("%[^\n]s",infix);

    infix_postfix(infix,postfix);
    printf("The postfix expression is: %s",postfix);
}
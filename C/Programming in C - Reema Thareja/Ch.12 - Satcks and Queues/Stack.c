#include <stdio.h>
#include <stdlib.h>

#define size 10

void display(int stack[],int *Top)
{
    int i;
    for (i=*Top;i>=0;i--)
    {
        printf("%d\n",stack[i]);
    }
}

void Push(int stack[],int *Top)
{
    if ((*Top)==size-1)
    {
        printf("Stack Overflow\n");
        return;
    }

    (*Top)++;
    printf("Enter the val to be added: ");
    scanf(" %d",&stack[*Top]);
}

int Pop(int stack[],int *Top)
{
    if ((*Top)==-1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
    (*Top)--;
    return stack[((*Top)+1)];
    }
}

int Peep(int stack[], int *Top)
{
    if ((*Top)==-1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        return (stack[*Top]);
    }
}


void Q1()
{
    int stack[size];
    int top=-1;
    int *Top=&top;

    int ch;
    do
    {
        printf("Enter your choice: ");
        scanf(" %d",&ch);

        switch(ch)
        {
            case 1:
            {
                display(stack,Top);
                break;
            }
            case 2:
            {
                Push(stack,Top);
                break;
            }
            case 3:
            {
                if ((*Top)==-1)
                {
                    printf("");
                }
                else
                {
                    printf("The val rem from stack is %d\n",Pop(stack,Top));
                    break;
                }
            }
            case 4:
            {
                if ((*Top)==-1)
                {
                    printf("");
                }
                else
                {
                    printf("The val at TOS is %d\n",Peep(stack,Top));
                    break;
                }
            }
        }
    } while (ch!=0);
}

void main()
{
    Q1();
}
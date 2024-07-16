#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
    int *arr;
    int size;
    int top;
}Stack;

Stack *new_stack()
{
    Stack *st=(Stack *)calloc(1,sizeof(Stack));
    printf("Enter the size of the array: ");
    scanf(" %d",&st->size);
    st->top=-1;
    st->arr=(int *)calloc(st->size,sizeof(int));
    return st;
}

int is_empty(Stack *st)
{
    if (st->top==-1)
    {
        //printf("Empty Stack\n");
        return 1;
    }
    else 
    {
        //printf("Stack is not empty");
        return 0;
    }
    
}

int is_full(Stack *st)
{
    if(st->top==st->size-1)
    {
        //printf("Stack is full\n");
        return 1;
    }
    else
    {
        //printf("Stack is not full\n");
        return 0;
    }
}

void display(Stack *st)
{
    if(is_empty(st))
    {
        printf("Empty Stack\n");
        return;
    }
    int i;
    for (i=st->top;i>=0;i--)
    {
        printf("%d\n",st->arr[i]);
    }
}

void push(Stack *st,int val)
{
    if(is_full(st))
    {
        printf("Stack is full\n");
        return ;
    }

    st->top++;
    st->arr[st->top]=val;
}

int pop(Stack *st)
{
    if (is_empty(st))
    {
        printf("Empty Stack\n");
        return 0;
    }
    st->top--;
    return (st->arr[st->top+1]);
}

int peek(Stack *st)
{
    if (is_empty(st))
    {
        printf("Empty Stack\n");
        return 0;
    }
    return (st->arr[st->top]);
}

void main()
{
    Stack *st1=new_stack();
    
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                display(st1);
                break;
            }            
            case 2:
            {
                if(is_empty(st1))
                    printf("Empty Stack\n");
                else
                    printf("Stack is not empty\n");
                break;
            }
            case 3:
            {
                if (is_full(st1))
                    printf("Stack is full\n");
                else 
                    printf("Stack is not full\n");
                break;
            }
            case 4:
            {
                int val;
                printf("Enter the val to be pushed: ");
                scanf(" %d",&val);
                push(st1,val);
                break;
            }
            case 5:
            {
                printf("Elem popped out of stack is %d\n",pop(st1));
                break;
            }
            case 6:
            {
                printf("The elem at TOS is %d\n",peek(st1));
                break;
            }
        }
    } while (ch!=0);
    
}
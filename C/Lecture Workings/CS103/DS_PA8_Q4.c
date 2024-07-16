#include <stdio.h>
#include <stdlib.h>

typedef struct st_node
{
    int data;
    struct st_node *next,*prev;
}st_node;

typedef struct stack
{
    st_node *top;
}St;

St *new_stack()
{
    St *st=(St *)calloc(1,sizeof(St));
    st->top=NULL;
    return st;
}

st_node *new_stack_node(int data)
{
    st_node *node=(st_node *)calloc(1,sizeof(st_node));
    node->data=data;
    node->next=NULL;
    node->prev=NULL;
    return node;
}

int is_empty(St *st)
{
    if(st->top==NULL)
    {
        return 1;
    }
    return 0;
}

void push(St *st,st_node *node)
{
    if(is_empty(st))
    {
        st->top=node;
    }
    else
    {
        st->top->next=node;
        node->prev=st->top;
        st->top=node;
    }
}

int pop(St *st)
{
    if(is_empty(st))
    {
        printf("Stack Underflow\n");
    }
    else
    {
        st_node *temp=st->top;
        int data=temp->data;
        st->top=temp->prev;
        if (st->top != NULL)
            st->top->next=NULL;
        free(temp);
        return(data);
    }
}

typedef struct q_st
{
    St *st1,*st2;
}q_st;

q_st *new_queue()
{
    q_st *q=(q_st *)calloc(1,sizeof(q_st));
    q->st1=new_stack();
    q->st2=new_stack();
    return q;
}

void enqueue(q_st **q,int data)
{
    push((*q)->st1,new_stack_node(data));
}

int dequeue(q_st **q)
{
    if(is_empty((*q)->st1))
    {
        printf("Queue is empty\n");
    }
    else 
    {
        while(!is_empty((*q)->st1))
        {
            push((*q)->st2,new_stack_node(pop((*q)->st1)));
        }

        int data=pop((*q)->st2);

        St *temp=(*q)->st1;
        (*q)->st1=(*q)->st2;
        (*q)->st2=temp; 

        return data;       
    }
}

void display(q_st *q)
{
    st_node *ptr=q->st1->top;

    if(is_empty(q->st1))
    {
        printf("Empty Queue\n");
        return;
    }

    while(!is_empty((q)->st1))
    {
       push((q)->st2,new_stack_node(pop((q)->st1)));
    }
    while(!is_empty(q->st2))
    {
        int data=pop(q->st2);
        printf("%d ",data);
        push(q->st1,new_stack_node(data));
    }
    printf("\n");    
}

void main()
{
    q_st *q=new_queue();
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                int data;
                printf("Enter the data: ");
                scanf(" %d",&data);
                enqueue(&q,data);
                break;
            }
            case 2:
            {
                printf("Elem dequeued is %d\n",dequeue(&q));
                break;
            }
            case 3:
            {
                display(q);
                break;
            }
        }
    } while (ch!=0);
    
}
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

typedef struct Q_node
{
    int data;
    struct Q_node *next,*prev;
}Q_node;

typedef struct que
{
    Q_node *f,*r;
}Q;

Q *new_queue()
{
    Q *q=(Q *)calloc(1,sizeof(Q));
    q->f=NULL;
    q->r=NULL;
    return q;
}

Q_node *new_queue_node(int data)
{
    Q_node *node=(Q_node *)calloc(1,sizeof(Q_node));
    node->next=NULL;
    node->prev=NULL;
    node->data=data;
    return node;
}

void enqueue(Q *q,int data)
{
    Q_node *node=new_queue_node(data);
    if(q->f==NULL)
    {
        q->f=node;
        q->r=node;
        return;
    }
    node->prev=q->r;
    q->r->next=node;
    q->r=node;
}

int dequeue(Q *q)
{
    if(q->f==NULL)
    {
        printf("Empty stack\n");
    }
    else 
    {
        Q_node *temp=q->f;
        int data=temp->data;
        temp->next->prev=NULL;
        q->f=temp->next;
        printf("hi\n");
        free(temp);
        printf("bye\n");
        return data;
    }
}

typedef struct stack
{
    Q *q1,*q2;
}St_Q;

St_Q *new_stack()
{
    St_Q *st=(St_Q *)calloc(1,sizeof(St_Q));
    st->q1=new_queue();
    st->q2=new_queue();
    return st;
}

void push(St_Q **st,int val)
{
    enqueue((*st)->q1,val);
}

int pop(St_Q **st)
{
    if((*st)->q1->f==NULL)
    {
        printf("Stack underflow\n");
    }
    else 
    {
        while((*st)->q1->f->next!=NULL)
        {
            enqueue((*st)->q2,dequeue((*st)->q1));
        }
        printf("go\n");
        int data=dequeue((*st)->q1);
        printf("%d\n",data);

        Q *temp=(*st)->q1;
        printf("ii\n");
        (*st)->q1=(*st)->q2;
        (*st)->q2=temp;
        printf("no\n");
        return data;
    }
}

void display(St_Q *st)
{
    Q_node *ptr=st->q1->r;

    while(ptr!=NULL)
    {
        printf("%d\n",ptr->data);
        ptr=ptr->prev;
    }
}

void main()
{
    St_Q *st=new_stack();
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch (ch)
        {
            case 1:
            {
                display(st);
                break;
            }
            case 2:
            {
                int val;
                printf("Enter the val to be pushed: ");
                scanf(" %d",&val);
                push(&st,val);
                break;
            }
            case 3:
            {
                printf("The popped out is %d\n",pop(&st));
                break;
            }
        }
    } while (ch!=0);
}
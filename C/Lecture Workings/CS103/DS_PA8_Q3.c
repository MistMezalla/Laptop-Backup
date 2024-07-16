#include <stdio.h>
#include <stdlib.h>

typedef struct queue_node
{
    int data;
    struct queue_node *next;
}Q_node;

typedef struct queue
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
    node->data=data;
    node->next=NULL;
    return node;
}

int is_empty(Q *q)
{
    if(q->f==NULL)
    {
        return 1;
    }
    else 
    return 0;
}

void enqueue(Q *q,Q_node *node)
{
    if(is_empty(q))
    {
        q->f=node;
        q->r=node;
    }
    q->r->next=node;
    q->r=node;
}

int dequeue(Q *q)
{
    if(is_empty(q))
    {
        printf("Queue is empty\n");
    }
    else 
    {
        int data;
        Q_node *temp=q->f;
        data=temp->data;
        q->f=temp->next;
        if(q->f==NULL)
            q->r==NULL;
        free(temp);
        return data;
    }
}

typedef struct st_q
{
    Q *q1,*q2;
}St_Q;

St_Q *new_st()
{
    St_Q *st=(St_Q *)calloc(1,sizeof(St_Q));
    st->q1=new_queue();
    st->q2=new_queue();
    return st;
}

void push(St_Q **st,int data)
{
    enqueue((*st)->q1,new_queue_node(data));
}

int pop(St_Q **st)
{
    if(is_empty((*st)->q1))
    {
        printf("Stack Underflow\n");
    }
    else if ((*st)->q1->f->next == NULL) 
    {
        return dequeue((*st)->q1); 
    }
    else
    {
        while((*st)->q1->f->next!=NULL)
        {
            enqueue((*st)->q2,new_queue_node(dequeue((*st)->q1)));
        }

        int data=dequeue((*st)->q1);

        Q *temp=(*st)->q1;
        (*st)->q1=(*st)->q2;
        (*st)->q2=temp;
        return data;
    }
}
/*
void rec_call(Q_node *ptr)
{
    if(ptr==NULL)
    return;
    ptr=ptr->next;
}

void display(St_Q *st)
{
    Q_node *ptr=st->q1->f;

    if(is_empty(st->q1))
    {
        printf("Empty Stack\n");
        return;
    }

    rec_call(ptr);
    printf("%d\n",ptr->data);
}
*/

void display(St_Q *st)
{
    Q_node *ptr = st->q1->f;

    if (is_empty(st->q1))
    {
        printf("Empty Stack\n");
        return;
    }

    if (st->q1->f->next == NULL) 
    {
        printf("%d\n", st->q1->f->data);
        return;
    }

    while (ptr != NULL)
    {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}

void main()
{
    St_Q *stack=new_st();
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
                printf("Enter the data to be pushed: ");
                scanf(" %d",&data);
                push(&stack,data);
                break;
            }
            case 2:
            {
                printf("The popped elem is %d\n",pop(&stack));
                break;
            }
            case 3:
            {
                display(stack);
                break;
            }
        }
    }while(ch!=0);
}
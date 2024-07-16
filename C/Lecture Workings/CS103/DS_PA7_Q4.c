#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int c,p;
    struct node *next,*prev;
}Node;

Node *new_node(int pow,int coeff)
{
    Node *node=(Node *)calloc(1,sizeof(Node));
    /*
    printf("Enter the power: ");
    scanf(" %d",&node->p);
    */
   node->p=pow;
   node->c=coeff;
   /*
    printf("Enter the coeff: ");
    scanf(" %d",&node->c);
    */
    node->next=node;
    node->prev=node;
    return node;
}

void add_first(Node **head,Node* node)
{
    if(*head==NULL)
    {
        *head=node;
        return;
    }
    node->next=*head;
    node->prev=(*head)->prev;
    (*head)->prev->next=node;
    (*head)->prev=node;
    *head=node;
}

void display(Node *head)
{
    Node *ptr=head;
    
    if(ptr->next==head)
    {
        printf("%d\n",ptr->c);
        return;
    }
    
    do
    {   
        printf("%dx^%d+",ptr->c,ptr->p);
        ptr=ptr->next;
    }while(ptr->next!=head);
    printf("%d\n",ptr->c);
}

void main()
{
    Node *p1=NULL;
    Node *p2=NULL;

    int d1,d2,i;
    int pow,coeff;
    printf("Enter the degree of poly 1: ");
    scanf(" %d",&d1);
    printf("The data of poly in asc order(pow,coeff): ");
    for (i=0;i<=d1;i++)
    {
        scanf(" %d %d",&pow,&coeff);
        add_first(&p1,new_node(pow,coeff));
    }
    display(p1);
    
    printf("Enter the degree of poly 2: ");
    scanf(" %d",&d2);
    printf("The data of poly in asc order(pow,coeff): ");
    for (i=0;i<=d2;i++)
    {
        scanf(" %d %d",&pow,&coeff);
        add_first(&p2,new_node(pow,coeff));
    }
    display(p2);

    Node *res=NULL;
    Node *ptr1=p1->prev,*ptr2=p2->prev;
    if(d1<=d2)
    {
        for (i=0;i<=d1;i++)
        {
            pow=ptr1->p;
            coeff=ptr1->c+ptr2->c;
            add_first(&res,new_node(pow,coeff));
            ptr1=ptr1->prev;
            ptr2=ptr2->prev;
        }
        for (i=d1+1;i<=d2;i++)
        {
            add_first(&res,new_node(ptr2->p,ptr2->c));
        }
    }
    else
    {
        for (i=0;i<=d2;i++)
        {
            pow=ptr2->p;
            coeff=ptr1->c+ptr2->c;
            add_first(&res,new_node(pow,coeff));
            ptr1=ptr1->prev;
            ptr2=ptr2->prev;
        }
        for (i=d2+1;i<=d1;i++)
        {
            add_first(&res,new_node(ptr1->p,ptr1->c));
        }
    }
    display(res);
}
#include <stdio.h>
#include <stdlib.h>

typedef struct node 
{
    int data;
    struct node * next;
}S_Node;

S_Node * new_node_S()
{
    S_Node *node;
    node=(S_Node *)calloc(1,sizeof(S_Node));
    
    printf("Enter the data: ");
    scanf(" %d",&node->data);
    
    node->next=NULL;

    return node;
}

void add_first(S_Node **head,S_Node *node)
{
    if(*head==NULL)
    {
        *head=node;
        return;
    }

    node->next=*head;
    *head=node;
}

void display(S_Node *head)
{
    S_Node *ptr=head;
    while(ptr!=NULL)
    {
        printf("%d ",ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}

void swap_nodes(S_Node **n1,S_Node **n2)
{
    int temp=(*n1)->data;
    (*n1)->data=(*n2)->data;
    (*n2)->data=temp;

    /*
    temp = (*n1)->next;
    (*n1)->next = (*n2)->next;
    (*n2)->next = temp;
    */
}

void Q1(S_Node **head);
//void Q5(S_Node *head);

void SL()
{
    S_Node *head=NULL;
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                display(head);
                break;
            }
            case 2:
            {
                add_first(&head,new_node_S());
                break;
            }
            case 3:
            {
                Q1(&head);
                break;
            }
            case 4:
            {
                Q5(head);
                break;
            }
        }
    } while (ch!=0);
}

void Q1(S_Node **head)
{
    S_Node *ptr,*preptr;
    preptr=*head;
    ptr=(*head)->next;
    //swap_nodes(&preptr,&ptr);
    //printf("%d %d\n",preptr->data,ptr->data);
    
    while(preptr!=NULL)
    {
        ptr = preptr->next;
        while(ptr!=NULL)
        {
            if(preptr->data>=ptr->data)
                swap_nodes(&preptr,&ptr);
            ptr=ptr->next;
        }
        preptr=preptr->next;
    }
    
    preptr=*head;
    while(preptr!=NULL)
    {
        ptr=preptr->next;
        if (ptr != NULL && ptr->data == preptr->data)
        {
            preptr->next=ptr->next;
            free(ptr);
        }
        preptr=preptr->next;
    }
}

void Q5(S_Node *head)
{
    S_Node *ptr=head;
    int flag=1;

    while(ptr->next!=NULL)
    {
        if(ptr->data>=ptr->next->data)
        {
            flag=0;
            break;
        }
        ptr=ptr->next;
    }
    if(flag)
        printf("Asc Oreder\n");
    else
        printf("Not Asc\n");
}

typedef struct node_C
{
    struct node_C *prev,*next;
    int data;
}Node_C;

Node_C *new_node_C()
{
    Node_C *node=(Node_C *)calloc(1,sizeof(Node_C));
    node->prev=node;
    node->next=node;
    printf("Enter the data: ");
    scanf(" %d",&node->data);
    
    return node;
}

void add_last(Node_C **head,Node_C *node)
{
    if (*head==NULL)
    {
        *head=node;
        return;
    }
    node->next=*head;
    node->prev=(*head)->prev;
    (*head)->prev->next=node;
    (*head)->prev=node;
}

void display_CD(Node_C *head)
{
    Node_C *ptr=head;
    if (head==NULL)
    {
        printf("Empty List\n");
        return;
    }

    do
    {
        printf("%d ",ptr->data);
        ptr=ptr->next;
    }while(ptr!=head);
    printf("\n");
}

void CD()
{
    Node_C *head=NULL;
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                display_CD(head);
                break;
            }
            case 2:
            {
                add_last(&head,new_node_C());
                break;
            }
            case 3:
            {
                Q7(head);
                break;
            }
        }
    } while (ch!=0);
}

void Q7(Node_C *head)
{
    Node_C *head_new=NULL;
    Node_C *ptr=head->prev;
    /*
    display_CD(head_new);
    add_last(&head_new,ptr);
    display_CD(head_new);
    */
    do
    {
        printf("%d ",ptr->data);
        Node_C node=()
        ptr=ptr->prev;
    }while(ptr!=head->prev);
    //printf("\nDone\n");
    display_CD(head_new);
    */
}

void main()
{
    CD();
}
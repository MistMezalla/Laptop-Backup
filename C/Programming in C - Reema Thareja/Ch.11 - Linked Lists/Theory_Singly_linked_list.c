#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} Node;

Node *new_node()
{
    Node *node = (Node *)calloc(1, sizeof(Node));
    printf("Enter the data: ");
    scanf(" %d", &node->data);
    node->next = NULL;

    return node;
}

void add_first(Node **head, Node *node)
{
    if (*head==NULL)
        *head = node;
    else
    {
        node->next=*head;
        *head=node;
    }
}

void add_last(Node **head, Node *node)
{
    //printf("Hi\n");
    Node *ptr;
    ptr=*head;

    if (*head==NULL)
        add_first(&(*head),node);
        
    else 
    {
        while(ptr->next!=NULL)
    {
        ptr=ptr->next;
    }
        //printf("AL: %d\n",ptr->data);
        ptr->next=node;
    }
    
}

void add_bef_val(Node **head,Node *node,int val)
{
    Node *ptr;//preptr;
    ptr=*head;

    if(ptr->data==val)
    {
        add_first(head,node);
        return;
    }

    while(ptr->next->data!=val)
    {
        //preptr=ptr;
        ptr=ptr->next;
    }

    node->next=ptr->next;
    ptr->next=node;
}

void add_after_val(Node **head,Node *node,int val)
{
    Node *ptr;//*preptr;
    ptr=*head;

    while(ptr->data!=val)
    {
        ptr=ptr->next;
    }

    node->next=ptr->next;
    ptr->next=node;
}

void display(Node *head)
{
    Node *ptr = head;
    while (ptr != NULL)
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
}

void del_first(Node **head)
{
    Node *ptr;
    ptr=*head;

    *head=(*head)->next;
    free(ptr);
}

void del_last(Node *head)
{
    Node *ptr;//*preptr;
    ptr=head;

    while(ptr->next->next!=NULL)
    {
        //preptr=ptr;
        ptr=ptr->next;
    }

    free(ptr->next);
    ptr->next=NULL;
}

void del_after_val(Node **head,int val)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(preptr->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    preptr->next=ptr->next;
    free(ptr);
}

void del_bef_val(Node **head,int val)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(ptr->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    preptr->next=ptr->next;
    free(ptr);
}

void rev_list(Node **head)
{
    Node *p,*c,*n;
    p=c=n=*head;
    n=n->next;

    while(n!=NULL)
    {
        p=c;
        c=n;
        n=n->next;
        c->next=p;
    }
    //n->next=c;
    (*head)->next=NULL;
    *head=c;
}

void Bsort_data(Node **head)
{
    Node *ptr,*preptr;
    preptr=*head;
    ptr=(*head)->next;
    int min=(*head)->data;

    while(preptr->next!=NULL)
    {
        while(ptr->next!=NULL)
        {
            if(ptr->data<=preptr->data)
            {
                int temp;
                temp=ptr->data;
                ptr->data=preptr->data;
                preptr->data=temp;
            }
            ptr=ptr->next;
        }
        preptr=preptr->next;
    }
}

void Isort_data(Node **head)
{
    Node *ptr,*preptr;
    preptr=*head;
    ptr=(*head)->next;

    int min=preptr->data;
    while(preptr->next!=NULL)
    {
        while(ptr->next!=NULL)
        {
            if(ptr->data<=min)
            {
                min=ptr->data;
            }
            ptr=ptr->next;
        }
    }
    
    preptr=ptr=*head;
    while(ptr->next!=NULL)
    {
        if (ptr->data==min)
            break;
        ptr=ptr->next;
    }

    int temp;
    temp=ptr->data;
    ptr->data=preptr->data;
    preptr->data=temp;

    ptr=(*head)->next;

    while(ptr->next!=NULL)
    {
        while(preptr->next!=ptr)
        {
            if (preptr->data<=ptr->data)
            {
                
            }
        }
    }
}

void Rec_dis_call(Node *node)
{
    if (node==NULL)
    {
        printf("\n");
        return;
    }
    printf("%d ",node->data);
    Rec_dis_call(node->next);
}

void rec_display(Node *head)
{
    Node *ptr;
    ptr=head;
    Rec_dis_call(ptr);
}

void Rec_rev_dis_call(Node *node)
{
    if (node==NULL)
    {
        return;
    }

    Rec_rev_dis_call(node->next);
    printf("%d ",node->data);
}

void rec_rev_display(Node *head)
{
    Node *ptr;
    ptr=head;
    Rec_rev_dis_call(ptr);
    printf("\n");
}

void Rec_rev_call(Node *p,Node *c, Node *n, Node **head)
{
    if(n==NULL)
    {
        n=c;
        (*head)->next=NULL;
        *head=n;
        //printf("Bye\n");
        return;
    }

    p=c;
    c=n;
    n=n->next;
    c->next=p;
    //printf("Hi\t");
    Rec_rev_call(p,c,n,head);
}

void rec_rev_list(Node **head)
{
    Node *p,*c,*n;
    p=c=n=*head;
    n=n->next;

    Rec_rev_call(p,c,n,head);
}

void Q1()
{
    Node *head = NULL;
    int ch;
    do
    {
        printf("Enter your choice: ");
        scanf(" %d",&ch);

        switch(ch)
        {
            case 1:
                new_node();
                break;
            case 2:
                display(head);
                break;
            case 3:
                add_first(&head, new_node());
                break;
            case 4:
                add_last(&head, new_node());
                break;
            case 5:
                {
                int bef_val;
                printf("Enter the before value: ");
                scanf(" %d",&bef_val);
                add_bef_val(&head,new_node(),bef_val);
                break;
                }
            case 6:
                {
                int aft_val;
                printf("Enter the after value: ");
                scanf(" %d",&aft_val);
                add_after_val(&head,new_node(),aft_val);
                break;
                }
                case 7:
                    del_first(&head);
                    break;
                case 8:
                    del_last(head);
                    break;
                case 9:
                {
                int bef_val;
                printf("Enter the before value: ");
                scanf(" %d",&bef_val);
                del_bef_val(&head,bef_val);
                break;
                }
            case 10:
                {
                int aft_val;
                printf("Enter the after value: ");
                scanf(" %d",&aft_val);
                del_after_val(&head,aft_val);
                break;
                }
            case 11:
                {
                    rev_list(&head);
                    break;
                }
            case 12:
                {
                    Bsort_data(&head);
                    break;
                }
            case 13:
                {
                    rec_display(head);
                    break;
                }
            case 14:
                {
                    rec_rev_display(head);
                    break;
                }
            case 15:
                {
                    rec_rev_list(&head);
                    break;
                }
        }
    } while(ch!=0);
}


void main()
{
    Q1();
}

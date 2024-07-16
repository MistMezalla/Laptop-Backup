#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next,*prev;
}Node;

Node *new_node()
{
    Node *node=(Node *)calloc(1,sizeof(Node));
    printf("Enter the data: ");
    scanf(" %d",&node->data);
    node->next=node;
    node->prev=node;

    return node;
}

void add_first(Node **head,Node *node)
{
    if (*head==NULL)
    {
        *head=node;
        //(*head)->next=(*head)->prev=node;
    }
    else
    {
        node->next=*head;
        node->prev=(*head)->prev;
        (*head)->prev->next=node;
        (*head)->prev=node;
        *head=node;
        //(*head)->next=node;
    }
}

void display_for(Node *head)
{
    if (head == NULL) 
    {
        printf("Empty List\n");
            return;
    }



    Node *ptr;
    ptr=head;
    do
    {
        printf("%d ",ptr->data);
        ptr=ptr->next;
    }while(ptr!=head);
    //printf("%d ",ptr->data);
    printf("\n");
}

void display_rev_test(Node *head)
{
    if (head == NULL) 
    {
        printf("Empty List\n");
            return;
    }

    Node *ptr;
    ptr=head;
    do
    {
        printf("%d\t",ptr->data);
        printf("%d ",ptr->prev->data);
        ptr=ptr->next;
    }while(ptr!=head->prev->prev);
    printf("%d ",ptr->data);
    printf("\n");
}

void display_rev(Node *head)
{
    if (head == NULL) 
    {
        printf("Empty List\n");
            return;
    }

    Node *ptr=head->prev;

    do
    {
        printf("%d ",ptr->data);
        ptr=ptr->prev;
    }while(ptr!=head->prev);
    printf("\n");
}

void add_last(Node **head, Node *node)
{
    if (*head==NULL)
    {
        add_first(&(*head),node);
        return;
    }

    node->next=*head;
    node->prev=(*head)->prev;
    (*head)->prev->next=node;
    (*head)->prev=node;
}

void add_after_val(Node **head,Node *node,int val)
{
    if (*head == NULL)
    {
        add_first(head,node);
        return;
    }
    Node *ptr=*head;

    while(ptr->data!=val)
    {
        ptr=ptr->next;
    }

    node->next=ptr->next;
    node->prev=ptr;
    ptr->next->prev=node;
    ptr->next=node;
}

void add_bef_val(Node **head,Node *node, int val)
{
    if (*head == NULL)
    {
        add_first(head,node);
        return;
    }
    Node *ptr=*head;

    while(ptr->next->data!=val)
    {
        ptr=ptr->next;
    }

    if (ptr->next==*head)
    {
        add_first(head,node);
        return;
    }

    node->next=ptr->next;
    node->prev=ptr;
    ptr->next->prev=node;
    ptr->next=node;
}

void del_first(Node **head)
{
    if (*head==NULL)
    {
        printf("Empty list\n");
        return;
    }

    Node *ptr=*head;
    (*head)->prev->next=ptr->next;
    (*head)=ptr->next;
    (*head)->prev=ptr->prev;
    if (ptr==ptr->next)
    {
        *head=NULL;
    }
    free(ptr);
}

void del_last(Node **head)
{
    if (*head==NULL)
    {
        printf("Empty list\n");
        return;
    }
    Node *ptr=(*head)->prev;
    //printf("%d\t",ptr->data);
    ptr->prev->next=*head;
    //printf("%d\t",ptr->prev->next->data);
    (*head)->prev=ptr->prev;
    //printf("%d\t",(*head)->prev->data);
    if (ptr==ptr->next)
    {
        *head=NULL;
    }
    free(ptr);      
}

void del_aft_val(Node **head,int val)
{
    if (*head==NULL)
    {
        printf("Empty List\n");
        return;
    }
    Node *ptr=*head;
    Node *preptr=*head;
    ptr=ptr->next;

    while(preptr->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    if (ptr==preptr)
        {
            printf("Singleton List\n");
            return;
        }
    if (preptr=(*head)->prev)
    {
        (*head)=ptr->next;
    }
    preptr->next=ptr->next;
    ptr->next->prev=preptr;
    free(ptr);
    //printf("%d\t%d",*head,(*head)->data);
}

void del_bef_val(Node **head,int val)
{
    if (*head==NULL)
    {
        printf("Empty List\n");
        return;
    }
    Node *ptr=*head;
    Node *preptr=*head;
    ptr=ptr->next;

    while(ptr->next->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    if (ptr==preptr)
        {
            printf("Singleton List\n");
            return;
        }

    if((*head)->prev==preptr)
    {
        *head=ptr->next;
    }

    preptr->next=ptr->next;
    ptr->next->prev=preptr;
    free(ptr);
}

int count_list(Node *head)
{
    Node *ptr=head;
    int c=1;

    while(ptr->next!=head)
    {
        c++;
        ptr=ptr->next;
    }
    return c;
}

void add_pos(Node **head,Node *node,int pos) //pos=1 and last giving LE
{
    if (*head==NULL)
    {
        add_first(head,node);
        return;
    }
    Node *ptr;//*preptr;
    ptr=*head;
    int i;

    for (i=1;i<pos;i++)
    {
        //preptr=ptr;
        ptr=ptr->next;
    }

    node->next=ptr;
    node->prev=ptr->prev;
    //printf("%d\t",node->prev->data);
    ptr->prev=node;
    ptr->prev->prev->next=node;
}

void del_pos(Node **head,int pos)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;
    int i;

    for(i=1;i<pos;i++)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    if (preptr==*head)
    {
        del_first(head);
        return;
    }
    preptr->next=ptr->next;
    ptr->next->prev=preptr;
    free(ptr);
}

int get_data(Node *head,int pos)
{
    Node *ptr=head;
    int i;
    for (i=1;i<pos;i++)
    {
        ptr=ptr->next;
    }

    return ptr->data;
}

void asc_sort(Node **head)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;
    //ptr=ptr->next;

    do
    {
        ptr=preptr->next;
        while(ptr!=*head)
        {
            if (preptr->data>=ptr->data)
            {
                int temp;
                temp=ptr->data;
                ptr->data=preptr->data;
                preptr->data=temp;
            }
            ptr=ptr->next;
        }
        preptr=preptr->next;
    }while(preptr->next!=*head);
}

void rev_list(Node **head) 
{
    if(*head==NULL)
    {
        printf("Empty List\n");
        return;
    }

    Node *p,*c,*n,*ptr;
    p=c=n=*head;
    n=n->next;
    int i=0;

    ptr=*head;
    while(ptr!=(*head)->prev)
    {
        ptr=ptr->next;
    }

    do
    {
        p=c;
        printf("%d\t",p->data);
        c=n;
        printf("%d\t",p->data);
        n=n->next;
        printf("%d\t",p->data);
        c->next=p;
        printf("%d\t",p->data);
        p->prev=c;
        printf("%d\n",p->data);
        //printf("\n%d\t%d\t%d\n",p->prev->data,c->next->data,n->data);
        i++;
    }while(p!=ptr);
    *head=ptr;
    printf("%d\n",(*head)->data);
    printf("%d\n",i);
}

void add_elem_sorted(Node **head,Node *node)
{
    Node *ptr=*head;
    Node *p=node;

    while(ptr->next!=*head)
    {
        if (ptr->data>=p->data)
        {
            add_bef_val(head,p,ptr->data);
        }
        ptr=ptr->next;
    }
}

void merge_lists(Node **head, Node **head1) 
{
    if (*head == NULL) 
        *head = *head1;
    else if (*head1 != NULL) 
    {
        Node *temp = (*head)->prev;
        (*head)->prev->next = (*head1);
        (*head)->prev = (*head1)->prev;
        (*head1)->prev->next = (*head);
        (*head1)->prev = temp;
    }
    *head1 = NULL;
}

void Rec_dis_call(Node *ptr,Node *head)
{   
    printf("%d ",ptr->data);
    if (ptr->next==head)
    {
        printf("\n");
        return;
    }
    Rec_dis_call(ptr->next,head);
}

void rec_display(Node *head)
{
    Rec_dis_call(head,head);
}

void Rec_rev_dis_call(Node *ptr,Node *hp)
{
    printf("%d ",ptr->data);
    if (ptr->prev==hp)
    {
        printf("\n");
        return;
    }
    Rec_rev_dis_call(ptr->prev,hp);
}

void rec_rev_display(Node *head)
{
    Rec_rev_dis_call(head->prev,head->prev);
}

void rev_rec(Node** head, Node* current) 
{
    if (*head == NULL) 
        return; 
    if (current->next == *head) 
    { 
        *head = current;
        return;
    }
    rev_rec(head, current->next);
    current->next->next = current;
    current->prev = current->next;
}

void main()
{
    Node *head=NULL;
    int ch;
    do
    {
        new_list:
        printf("Enter the choice: ");
        scanf(" %d",&ch);

        switch(ch)
        {
            case 1:
                {
                    display_for(head);
                    break;
                }
            case 2:
                {
                    display_rev(head);
                    break;
                }
            case 3:
                {
                    add_first(&head,new_node());
                    break;
                }
            case 4:
                {
                    add_last(&head,new_node());
                    break;
                }
            case 5:
                {
                    int val;
                    printf("Enter the after val: ");
                    scanf(" %d",&val);

                    add_after_val(&head,new_node(),val);
                    break;
                }
            case 6:
                {
                    int val;
                    printf("Enter the before val: ");
                    scanf(" %d",&val);

                    add_bef_val(&head,new_node(),val);
                    break;
                }
            case 7:
                {
                    del_first(&head);
                    break;
                }
            case 8:
                {
                    del_last(&head);
                    break;
                }
            case 9:
                {
                    int val;
                    printf("Enter the after val to be deleted: ");
                    scanf(" %d",&val);
                    del_aft_val(&head,val);
                    break;
                }
            case 10:
                {
                    int val;
                    printf("Enter the bef val to be deleted: ");
                    scanf(" %d",&val);
                    del_bef_val(&head,val);
                    break;
                }
            case 11:
                {
                    printf("%d\n",count_list(head));
                    break;
                }
            case 12:
                {
                    int pos;
                    printf("Enter the position where elem is to be added :");
                    scanf(" %d",&pos);
                    add_pos(&head,new_node(),pos);
                    break;
                }
            case 13:
                {
                    int pos;
                    printf("Enter the position where elem is to be deleted :");
                    scanf(" %d",&pos);
                    del_pos(&head,pos);
                    break;
                }
            case 14:
                {
                    int pos;
                    printf("Enter the position where elem is to be extracted:");
                    scanf(" %d",&pos);
                    if (pos>count_list(head))
                        break;
                    printf("The elem at pos %d is %d\n",pos,get_data(head,pos));
                    break;
                }
            case 15:
                {
                    asc_sort(&head);
                    break;
                }
            case 16:
                {
                    add_elem_sorted(&head,new_node());
                    break;
                }
            case 17:
                {
                    Node *head1=NULL;
                    int choice;
                    do
                    {
                        printf("Enter the choice for new list: ");
                        scanf(" %d",&choice);
                        add_first(&head1,new_node());
                        //goto new_list;
                    }while(choice!=0);
                    
                    merge_lists(&head,&head1);
                    break;
                }
            case 18:
                {
                    rev_list(&head);
                    break;
                }
            case 19:
                {
                    rec_display(head);
                    break;
                }
            case 20:
                {
                    rec_rev_display(head);
                    break;
                }
            case 21:
                {
                    rev_rec(&head, head);
                    break;
                }
        }
    }while(ch!=0);
    
}
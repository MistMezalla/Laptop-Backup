#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *prev,*next;
}Node;

Node *new_node()
{
    Node *node=(Node *)calloc(1,sizeof(Node));
    node->next=NULL;
    node->prev=NULL;
    printf("Enter the data: ");
    scanf(" %d",&node->data);

    return node;
}

void dis_for(Node *head,Node *tail)
{
    Node *ptr=head;
    if(head==NULL)
    {
        printf("Empty\n");
        return;
    }

    while(ptr!=NULL)
    {
        printf("%d ",ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}

void dis_rev(Node *head,Node *tail)
{
    Node *ptr=tail;
    if(head==NULL)
    {
        printf("Empty\n");
        return;
    }

    while(ptr!=NULL)
    {
        printf("%d ",ptr->data);
        ptr=ptr->prev;
    }
    printf("\n");
}

void add_first(Node **head,Node **tail,Node *node)
{
    if(*head==NULL)
    {
        *head=node;
        *tail=node;
        return;
    }
    
    node->next=*head;
    (*head)->prev=node;
    *head=node;
}

void add_last(Node **head,Node **tail,Node *node)
{
    if(*head==NULL)
    {
        add_first(head,tail,node);
        return;
    }

    node->prev=*tail;
    (*tail)->next=node;
    *tail=node;
}

void add_bef_val(Node **head,Node **tail,Node *node,int val)
{
    Node *ptr=*head;
    
    if(ptr->data==val)
    {
        add_first(head,tail,node);
        return;
    }

    while(ptr!=NULL)
    {
        if(ptr->next->data==val)
            break;
        ptr=ptr->next;
    }

    node->prev=ptr;
    node->next=ptr->next;
    ptr->next->prev=node;
    ptr->next=node;
}

void add_aft_val(Node **head,Node **tail,Node *node,int val)
{
    Node *ptr=*head;
    
    while(ptr!=NULL)
    {
        if(ptr->data==val)
        {
            if(ptr==*tail)
            {
                add_last(head,tail,node);
                return;
            } 
            break;
        }
        ptr=ptr->next;
    }

    node->prev=ptr;
    node->next=ptr->next;
    ptr->next->prev=node;
    ptr->next=node;
}

void del_first(Node **head,Node **tail)
{
    Node *ptr=*head;

    if(*head==NULL)
    {
        printf("Empty list\n");
        return;
    }
    
    (*head)->next->prev=NULL;
    *head=(*head)->next;
    free(ptr);
}

void del_last(Node **head,Node **tail)
{
    Node *ptr=*tail;
    if(*head==NULL)
    {
        printf("Empty List\n");
    }

    ptr->prev=(*tail)->prev;
    ptr->next=NULL;
    *tail=ptr->prev;
    free(ptr);
}

void del_bef_val(Node **head,Node **tail,int val)//,Node *node,int val)
{
    Node *ptr=*head;

    while(ptr!=NULL)
    {
        if(ptr->next->data==val)
            break;
        ptr=ptr->next;
    }

    if(ptr==*head)
    {
        del_first(head,tail);
        return;
    }

    ptr->prev->next=ptr->next;
    ptr->next->prev=ptr->prev;
    free(ptr);
}

void del_aft_val(Node **head,Node **tail,int val)
{
    Node *ptr=*head;
    if(*head==NULL)
    {
        printf("Empty List\n");
        return;
    }

    while(ptr!=NULL)
    {
        if(ptr->prev->data==val)
            break;
        ptr=ptr->next;
    }

    if(ptr->next==*tail)
    {
        del_last(head,tail);
        return;
    }

    ptr->prev->next=ptr->next;
    ptr->next->prev=ptr->prev;
    free(ptr);
}

int count(Node *head,Node *tail)
{
    Node *ptr=head;
    int c=0;

    while(ptr!=NULL)
    {
        ptr=ptr->next;
        c++;
    }

    return c;
}

void add_data_pos(Node **head,Node **tail,Node *node,int pos)
{
    Node *ptr=*head;
    int i;

    for (i=1;i<pos;i++)
    {
        ptr=ptr->next;
    }

    if(ptr==*head)
    {
        add_first(head,tail,node);
        return;
    }

    if(ptr==*tail)
    {
        add_last(head,tail,node);
        return;
    }

    node->prev=ptr;
    node->next=ptr->next;
    ptr->next->prev=node;
    ptr->next=node;
}

void del_data_pos(Node **head,Node **tail,int pos)
{
    Node *ptr=*head;
    int i;

    for (i=1;i<pos;i++)
    {
        ptr=ptr->next;
    }

    if(ptr==*head)
    {
        del_first(head,tail);
        return;
    }

    if(ptr==*tail)
    {
        del_last(head,tail);
        return;
    }

    ptr->prev->next=ptr->next;
    ptr->next->prev=ptr->prev;
    free(ptr);
}

int get_data_pos(Node *head,Node *tail,int pos)
{
    Node *ptr=head;

    int i;
    for (i=1;i<pos;i++)
    {
        ptr=ptr->next;
    }

    return(ptr->data);
}

void asc_sort_data(Node **head)
{
    Node *ptr,*preptr;
    preptr=*head;
    ptr=(*head)->next;

    while(preptr!=NULL)
    {
        while(ptr!=NULL)
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

void ins_elem_sorted(Node **head,Node **tail,Node *node)
{
    Node *ptr=*head;
    int pos=1;

    while(ptr!=NULL)
    {
        if(ptr->next->data>=node->data)
            break;
        pos++;
        ptr=ptr->next;
    }

    add_data_pos(head,tail,node,pos);
}

void rev_list(Node **head,Node **tail)
{
    Node *ptr=*head;

    while(ptr!=NULL)
    {
        if(ptr==*head)
        {
            *tail=ptr;
        }
        else if(ptr->next==NULL)
        {
            *head=ptr;
        }
        Node *temp;
        temp=ptr->next;
        ptr->next=ptr->prev;
        ptr->prev=temp;

        ptr=ptr->prev;
    }
}

void Rec_dis_call(Node *ptr,Node *head)
{   
    printf("%d ",ptr->data);
    if (ptr->next==NULL)
    {
        printf("\n");
        return;
    }
    Rec_dis_call(ptr->next,head);
}

void rec_display(Node *head,Node *tail)
{
    Rec_dis_call(head,head);
}

void Rec_rev_dis_call(Node *ptr, Node *tail)
{
    printf("%d ", ptr->data);
    if (ptr == tail)
    {
        printf("\n");
        return;
    }
    Rec_rev_dis_call(ptr->next, tail);
}

void rec_rev_display(Node *head, Node *tail)
{
    Rec_rev_dis_call(head, tail);
}

void Rev_rec_call(Node *ptr)
{
    if (ptr == NULL)
        return;
    Node *temp = ptr->next;
    ptr->next = ptr->prev;
    ptr->prev = temp;
    if (ptr->prev == NULL) 
        return;
    Rev_rec_call(ptr->prev);
}

void rev_rec(Node **head, Node **tail)
{
    if (*head == NULL || *head == *tail)
        return; 
    Rev_rec_call(*head);

    Node *temp = *head;
    *head = *tail;
    *tail = temp;
}

void merge_lists(Node **ptr1, Node **ptr2)
{
    Node *tail1 = (*ptr1)->prev;
    Node *head2 = *ptr2;

    tail1->next = head2;
    head2->prev = tail1;

    (*ptr2)->prev = tail1;

    *ptr1 = *ptr1;
}

void mergeSortedLists(Node  **ptr1, Node **ptr2)
{
    merge_lists(ptr1,ptr2);
    asc_sort(ptr1);
}

void main()
{
    Node *head=NULL;
    Node *tail=NULL;
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                dis_for(head,tail);
                break;
            }
            case 2:
            {
                dis_rev(head,tail);
                break;
            }
            case 3:
            {
                add_first(&head,&tail,new_node());
                break;
            }
            case 4:
            {
                add_last(&head,&tail,new_node());
                break;
            }
            case 5:
            {
                int val;
                printf("Enter the bef value to be added: ");
                scanf(" %d",&val);
                add_bef_val(&head,&tail,new_node(),val);
                break;
            }
            case 6:
            {
                int val;
                printf("Enter the after value to be added: ");
                scanf(" %d",&val);
                add_aft_val(&head,&tail,new_node(),val);
                break;
            }
            case 7:
            {
                del_first(&head,&tail);
                break;
            }
            case 8:
            {
                del_last(&head,&tail);
                break;
            }
            case 9:
            {
                int val;
                printf("Enter the bef val to be delted: ");
                scanf(" %d",&val);
                del_bef_val(&head,&tail,val);
                break;
            }
            case 10:
            {
                int val;
                printf("Enter the aft val to be delted: ");
                scanf(" %d",&val);
                del_aft_val(&head,&tail,val);
                break;
            }
            case 11:
            {
                printf("%d\n",count(head,tail));
                break;
            }
            case 12:
            {
                int pos;
                printf("Enter the pos: ");
                scanf(" %d",&pos);
                add_data_pos(&head,&tail,new_node(),pos);
                break;
            }
            case 13:
            {
                int pos;
                printf("Enter the pos: ");
                scanf(" %d",&pos);
                del_data_pos(&head,&tail,pos);
                break;
            }
            case 14:
            {
                int pos;
                printf("Enter the pos: ");
                scanf(" %d",&pos);
                printf("The data at pos %d is %d\n",pos,get_data_pos(head,tail,pos));
                break;
            }
            case 15:
            {
                asc_sort_data(&head);
                break;  
            }
            case 16:
            {
                ins_elem_sorted(&head,&tail,new_node());
                break;
            }
            case 17:
            {
                rev_list(&head,&tail);
                break;
            }
            case 18:
            {
                rec_display(head,tail);
                break;
            }
            case 19:
            {
                rec_rev_display(head,tail);
                break;
            }
            case 20:
            {
                rev_rec(&head,&tail);
                break;
            }
            case 21:
            {
                Node *head1=NULL;
                Node *tail1=NULL;
                Node *head2=NULL;
                Node *tail2=NULL;
                
                add_first(head1,tail1,new_node());
                add_first(head1,tail1,new_node());
                add_first(head1,tail1,new_node());

                add_first(head2,tail2,new_node());
                add_first(head2,tail2,new_node());

                merge_lists(&head1,&head2);
                dis_for(head1,tail1);
                break;
            }
            case 22:
            {
                Node *head1=NULL;
                Node *tail1=NULL;
                Node *head2=NULL;
                Node *tail2=NULL;
                
                add_first(head1,tail1,new_node());
                add_first(head1,tail1,new_node());
                add_first(head1,tail1,new_node());

                add_first(head2,tail2,new_node());
                add_first(head2,tail2,new_node());

                asc_sort(&head1);
                asc_sort(&head2);

                mergeSortedLists(&head1,&head2);
                dis_for(head1,tail1);
                break;
            }
        }
    } while (ch!=0);
}
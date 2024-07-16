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
        *head = node;
}

void add_last(Node **head, Node *node)
{
    //printf("Hi\n");
    Node *ptr;
    ptr=*head;

    if (*head==NULL)
        printf("Error");

    while(ptr->next!=NULL)
    {
        ptr=ptr->next;
    }
    //printf("AL: %d\n",ptr->data);
    ptr->next=node;
}

void add_bef_val(Node **head,Node *node,int val)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(ptr->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    preptr->next=node;
    node->next=ptr;
}

void add_after_val(Node **head,Node *node,int val)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(preptr->data!=val)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    preptr->next=node;
    node->next=ptr;
}

void display(Node **head)
{
    Node *ptr = *head;
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

void del_last(Node **head)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(ptr->next!=NULL)
    {
        preptr=ptr;
        ptr=ptr->next;
    }

    preptr->next=NULL;
    free(ptr);
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

int count_list(Node **head)
{
    Node *ptr;
    ptr=*head;
    int c=0;
    
    while(ptr!=NULL)
    {
        c++;
        ptr=ptr->next;
    }
    return c;
}

int elem_pos(Node **head,int pos)
{
    Node *ptr;
    ptr=*head;
    int c=0;

    while(ptr!=NULL)
    {
        c++;
        if (c==pos)
            break;
        ptr=ptr->next;
    }
    return ptr->data;
}

void set_elem(Node **head,int pos,int val)
{
    Node *ptr;
    ptr=*head;
    int c=0;
    while(ptr!=NULL)
    {
        c++;
        if (c==pos)
            break;
        ptr=ptr->next;
    }
    ptr->data=val;
}

void add_elem(Node **head,int pos)
{
    Node *ptr,*preptr,*node;
    ptr=preptr=*head;
    int c=0;
    node=new_node();

    while(ptr!=NULL)
    {
        c++;
        if (c==pos)
            break;
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=node;
    node->next=ptr;
}

void del_elem_pos(Node **head,int pos)
{
     Node *ptr,*preptr;
    ptr=preptr=*head;
    int c=0;

    while(ptr!=NULL)
    {
        c++;
        if (c==pos)
            break;
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=ptr->next;
    free(ptr);
}

void rem_elem(Node **head,int val)
{
    Node *ptr,*preptr;
    ptr=preptr=*head;

    while(ptr!=NULL)
    {
        if(ptr->data==val)
            break;
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=ptr->next;
    free(ptr);
}

void asc_sort(Node **head)
{
    Node *current, *next;
    int temp;
    int swapped;

    do 
    {
        swapped = 0;
        current = *head;

        while (current->next != NULL) 
        {
            next = current->next;

            if (current->data > next->data) 
            {
                temp = current->data;
                current->data = next->data;
                next->data = temp;
                swapped = 1;
            }

            current = current->next;
        }
    } while (swapped);

    printf("List sorted in ascending order: ");
    display(head);
}

void reverse_list(Node **head) 
{
    Node *current = *head;
    Node *prev = NULL;
    Node *next = NULL;

    while (current != NULL) 
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

void insert_sorted(Node **head, int value) 
{
    Node *newNode = (Node *)calloc(1, sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;

    if (*head == NULL || value <= (*head)->data) 
    {
        newNode->next = *head;
        *head = newNode;
    } 
    else 
    {
        Node *current = *head;
        Node *prev = NULL;

        while (current != NULL && current->data < value) 
        {
            prev = current;
            current = current->next;
        }

        prev->next = newNode;
        newNode->next = current;
    }
}

void print_list_recursive(Node *head)
{
    if (head == NULL) 
    {
        printf("\n");
        return;
    }

    printf("%d ", head->data);
    print_list_recursive(head->next);
}

void print_reverse_recursive(Node *head)
{
    if (head == NULL) 
        return;

    print_reverse_recursive(head->next);
    printf("%d ", head->data);
}

Node * reverse_list_recursive(Node *current, Node *prev)
{
    if (current == NULL) 
        return prev;

    Node *next = current->next;
    current->next = prev;
    
    return reverse_list_recursive(next, current);
}

void main()
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
                display(&head);
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
                    del_last(&head);
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
                printf("Number of elements in the list are: %d\n",count_list(&head));
                break;
            case 12:
                {
                    int pos;
                    printf("Enter the postion: ");
                    scanf(" %d",&pos);
                    printf("The element at %d is: %d\n",pos,elem_pos(&head,pos));
                    break;
                }
            case 13:
                {
                    int pos,val;
                    printf("Enter the postion and the value to be set: ");
                    scanf(" %d %d",&pos,&val);
                    set_elem(&head,pos,val);
                    break;
                }
            case 14:
                {
                    int pos;
                    printf("Enter the postion where element is to be added: ");
                    scanf(" %d",&pos);
                    add_elem(&head,pos);
                    break;
                }
            case 15:
                {
                    int pos;
                    printf("Enter the postion from where element is to be deleted: ");
                    scanf(" %d",&pos);
                    del_elem_pos(&head,pos);  
                    break;
                }
            case 16:
                {
                    int val;
                    printf("Enter the element to be removed: ");
                    scanf(" %d",&val);
                    rem_elem(&head,val);
                    break;
                }
            
            case 17:
                {
                    asc_sort(&head);
                    break;
                }
            
            case 18:
                {
                    reverse_list(&head);
                    break;
                }
            case 19:
                {
                    int val;
                    printf("Enter the element to be inserted: ");
                    scanf(" %d", &val);
                    insert_sorted(&head, val);
                    break;
                }
            case 20:
                {
                printf("List: ");
                print_list_recursive(head);
                break;
                }
            case 21:
                {
                printf("List in reverse order: ");
                print_reverse_recursive(head);
                printf("\n");
                break;
                }
            case 22:
                {
                head = reverse_list_recursive(head, NULL);
                printf("List reversed.\n");
                break;
                }
        }
    } while(ch!=0);
}


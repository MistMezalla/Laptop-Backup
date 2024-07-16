#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
    int roll;
    char name[20];
}student;

typedef struct node
{
    student st;
    struct node *next;
}Node;

Node *new_node()
{
    Node *node=(Node *)calloc(1,sizeof(Node));

    printf("Enter the name of the student: ");
    scanf(" %[^\n]s",&node->st.name);

    printf("Enter the roll number of the student: ");
    scanf(" %d",&node->st.roll);

    node->next=NULL;

    return node;
}

void add_first(Node **head,Node *node)
{
    if (*head=NULL)
    {
        *head=node;
        return;
    }

    node->next=*head;
    *head=node;
}

void display(Node *head)
{
    Node *ptr=head;

    while(ptr!=NULL)
    {
        printf("%s\t%d\n",ptr->st.name,ptr->st.roll);
        ptr=ptr->next;
    }
}

void main()
{
    Node *head=NULL;

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
                    add_first(&head,new_node());
                    break;
                }
        }
    }while(ch!=0);
}
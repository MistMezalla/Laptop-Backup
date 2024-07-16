#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>

typedef struct node
{
    struct node *n;
    int data;
}Node;

Node *new_node(int data)
{
    Node *node=(Node *)calloc(1,sizeof(Node));
    node->data=data;
    node->n=NULL;

    return node;
}

void add_first(Node **head,int data)
{
    if(!(*head))
    {
        printf("%d\n",__LINE__);
        *head=new_node(data);
        return;
    }
    Node *node=new_node(data);
    node->n=*head;
    *head=node;
}

void add_last(Node **head,int data)
{
    if(!(*head))
    {
        //printf("%d\n",__LINE__);
        add_first(head,data);
        return;
    }

    Node *ptr=*head;
    /*
    if(!ptr->n)
    {
        printf("%d\n",__LINE__);
        ptr->n=new_node(data);
        return;
    }
    */
    while(ptr->n)
    {
        //printf("%d\n",__LINE__);
        ptr=ptr->n;
    }
    ptr->n=new_node(data);
}

void display(Node *node)
{
    while (node)
    {
        printf("%d ",node->data);
        node=node->n;
    }
    printf("\n");
}

void main()
{
    Node *Head=NULL;
    
    int ch;
    do
    { 
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                //printf("%d\n",__LINE__);
                int n=7;
                int arr[]={5,6,-7,19,-1,0,27,16,-23};

                int i;
                for (i=0;i<n;i++)
                {
                    //printf("%d\n",__LINE__);
                    add_last(&Head,arr[i]);
                }
                break;
            }
            case 2:
            {
                display(Head);
                break;
            }
        }

    } while (ch!=0);
    
}
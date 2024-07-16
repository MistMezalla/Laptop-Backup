#include <stdio.h>
#include <stdlib.h>

typedef struct tree
{
    struct tree *l,*r,*p;
    int data;
}Tree;

Tree *new_node(Tree **parent,int data)
{
    Tree *node=(Tree *)calloc(1,sizeof(Tree));
    node->data=data;
    node->l=NULL;
    node->r=NULL;
    node->p=*parent;
    return node;
}

void add_node(Tree **node,int data)
{
    if(*node==NULL)
   {
    *node=new_node(node,data);
    return;
   }
    if(data<=(*node)->data)
    {
        add_node(&(*node)->l,data);
    }
    else 
    {
        add_node(&(*node)->r,data);
    }
}

void pre_order(Tree *root)
{
    if(root!=NULL)
    {
        printf("%d ",root->data);
        pre_order(root->l);
        pre_order(root->r);
    }
}

void in_order(Tree *root)
{
    if(root!=NULL)
    {
        in_order(root->l);
        printf("%d ",root->data);
        in_order(root->r);
    }
}

void post_order(Tree *root)
{
   if(root!=NULL)
    {
        post_order(root->l);
        post_order(root->r);
        printf("%d ",root->data);
    }
}

typedef struct que_node
{
    int data;
    struct que_node *next;
}Q_node;

typedef struct que
{
    Q_node *f,*r;
}Q;

Q_node *new_node_q(int data)
{
    Q_node *node=(Q_node *)calloc(1,sizeof(Q_node));
    node->data=data;
    node->next=NULL;
    return node;
}

Q *new_queue()
{
    Q *q=(Q *)calloc(1,sizeof(Q));
    q->f=NULL;
    q->r=NULL;
    return q;
}

void enqueue(Q **q,int data)
{
    Q_node *node=new_node_q(data);
    if((*q)->f==NULL)
    {
        (*q)->f=node;
        (*q)->r=node;
        return;
    }
    (*q)->r->next=node;
    (*q)->r=node;
}

Q_node *dequeue(Q **q)
{
    Q_node *temp=(*q)->f;
    (*q)->f=temp->next;
    return temp;
}

void lvl_order(Tree *root)
{
    Q *q=new_queue();
    enqueue(&q,root->data);

    while(q->f!=NULL)
    {
        Tree *current=dequeue(&q);

        printf("%d ",current->data);

        if(current->l!=NULL)
        {
            enqueue(&q,current->l->data);
        }
        if(current->r!=NULL)
        {
            enqueue(&q,current->r->data);
        }
    }
}

void main()
{
    int data;
    printf("Enter the data of the root node: ");
    scanf(" %d",&data);
    Tree *root=new_node(&root,data);
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                pre_order(root);
                printf("\n");
                break;
            }
            case 2:
            {
                in_order(root);
                printf("\n");
                break;
            }
            case 3:
            {
                post_order(root);
                printf("\n");
                break;
            }
            case 4:
            {
                lvl_order(root);
                printf("\n");
                break;
            }
            case 5:
            {
                int data;
                printf("Enter the data: ");
                scanf(" %d",&data);
                add_node(&root,data);
                break;
            }
        }
    } while (ch!=0);
    
}
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    struct node *l,*p,*r;
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

Tree *par=NULL;
void add_node_bt(Tree **root,int data)
{
    if(!(*root))
    {
        *root=new_node(&par,data);
        return;
    }
    if((rand()%4)-2>=0)
    {
        if(!(*root)->l)
            par=*root;
        add_node_bt(&(*root)->l,data);
    }
    else
    {
        if(!(*root)->r)
            par=*root;
        add_node_bt(&(*root)->r,data);
    }
}

void in_order(Tree *root)
{
    if(root)
    {
        in_order(root->l);
        printf("%d ",root->data);
        in_order(root->r);
    }
}

void spaces(int n)
{
    int i;
    for (i=0;i<n;i++)
    {
        printf(" ");
    }
}

void tree_hori(Tree *root,int sp)
{
    if(!root)
        return;
    
    sp+=5;

    tree_hori(root->r,sp);

    printf("\n");
    spaces(sp);
    printf("%d\n",root->data);
    
    tree_hori(root->l,sp);
}

void draw_tree(Tree *root)
{
    tree_hori(root,0);
}

void num_nodes(Tree **root,int *c)
{
    if(*root)
    {
        num_nodes(&(*root)->l,c);
        (*c)++;
        num_nodes(&(*root)->r,c);
    }
}

int arr[100];
int k=0;

void nodes_trav(Tree **root)
{
    printf("%d\n",__LINE__);
    if(*root)
    {
        nodes_trav(&(*root)->l);
        arr[k]=(*root)->data;
        k++;
        nodes_trav(&(*root)->r);
    }
    
}

void nodes_cpy(Tree **root)
{
    printf("%d\n",__LINE__);
    if(*root)
    {
        nodes_cpy(&(*root)->l);
        (*root)->data=arr[k];
        k++;
        nodes_cpy(&(*root)->r);
    }
}

void bt_to_bst(Tree **root)
{
    int n=0;
    int *c=&n;
    num_nodes(root,c);
    printf("%d\n",__LINE__);
    nodes_trav(root);
    printf("%d\n",__LINE__);

    printf("%d\t%d\n",arr[0],n);
    int i;
    int j;

    for(i=0;i<n;i++)
    {
        printf("1 ");
    }
    printf("\n");

    for (i=0;i<n;i++)
    {
        printf("%d\n",__LINE__);
        for(j=i;j<n;j++)
        {
            printf("%d\n",__LINE__);
            if(arr[i]>=arr[j])
            {
                printf("%d\n",__LINE__);
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }

    printf("%d\n",__LINE__);
    k=0;
    nodes_cpy(root);
    printf("%d\n",__LINE__);
}

void main()
{
    int data;
    printf("Enter the root data: ");
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
                printf("The in order representation: \n");
                in_order(root);
                printf("\n");
                break;
            }
            case 2:
            {
                int n=4;
                int arr[]={2,7,8,4};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bt(&root,arr[i]);
                }
                break;
            }
            case 3:
            {
                draw_tree(root);
                printf("\n");
                break;
            }
            case 4:
            {
                printf("The in order representation of bst: \n");
                bt_to_bst(&root);
                in_order(root);
                draw_tree(root);
                printf("\n");
                break;
            }
        }
    } while (ch!=0);
    
}
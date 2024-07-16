#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    struct node *l,*p,*r;
    int data;
}Tree;

Tree *new_node(Tree **parent,int data)
{
    printf("%d\n",__LINE__);
    Tree *node=(Tree *)calloc(1,sizeof(Tree));
    node->data=data;
    node->l=NULL;
    node->r=NULL;
    node->p=*parent;

    return node;
}

Tree *par=NULL;
void add_node_bst(Tree **root,int data)
{
    if(!(*root))
    {
        printf("%d\n",__LINE__);
        if(par)
        printf("%d\n",par->data);
        *root=new_node(&par,data);
        return;
    }
    if(data<=(*root)->data)
    {
        printf("%d\n",__LINE__);
        if(!(*root)->l)
        {
             par=*root;
             printf("%d\n",__LINE__);
        }
           printf("%d\n",__LINE__);
        add_node_bst(&(*root)->l,data);
    }
    else
    {
        printf("%d\n",__LINE__);
        if(!(*root)->r)
             {
             par=*root;
             printf("%d\n",__LINE__);
        }
    printf("%d\n",__LINE__);
        add_node_bst(&(*root)->r,data);
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

Tree *node=NULL;
Tree *sec_largest_bst(Tree *root,int *c)
{
    if(node)
        return node;
    if(root)
    {
        node=sec_largest_bst(root->r,c);
        //(*c)++;
        
        if(*c==2)
        {
            if(!node)
                node=root;
        }
            
        else
            (*c)++;
        
        sec_largest_bst(root->l,c);
    }
    return node;
}

void main()
{
    int data;
    printf("Enter the root data: ");
    scanf(" %d",&data);
    Tree *root=new_node(&root,data);
    printf("%d\n",__LINE__);
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
                int n=1;
                int arr[]={5};
                int i;
                for (i=0;i<n;i++)
                {
                    printf("%d\n",__LINE__);
                    add_node_bst(&root,arr[i]);
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
                int c=1;
                int *cnt=&c;
                printf("%d\n",sec_largest_bst(root,cnt)->data);
                break;
            }
        }
    } while (ch!=0);
    
}
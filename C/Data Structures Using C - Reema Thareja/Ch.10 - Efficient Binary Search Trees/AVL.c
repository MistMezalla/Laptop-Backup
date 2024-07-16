#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *l,*p,*r;
}AVL;

AVL *new_node(AVL **parent,int data)
{
    AVL *node=(AVL *)calloc(1,sizeof(AVL));

    node->data=data;
    node->l=NULL;
    node->r=NULL;
    node->p=*parent;

    return node;
}

AVL *par=NULL;
void add_node_bst(AVL **root,int data)
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

void in_order(AVL *root)
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

void tree_hori(AVL *root,int sp)
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

void draw_tree(AVL *root)
{
    tree_hori(root,0);
}

void Right_rotate(AVL **root)
{
    AVL *A=*root,*B=(*root)->l;
    A->l=B->r;
    B->r->p=A;
    A->p=B;
    B->r=A;
    B->p=B;

    *root=B;
}

void Left_rotate(AVL **root)
{
    AVL *A=*root,*B=(*root)->r;
    A->r=B->l;
    B->l->p=A;
    A->p=B;
    B->l=A;
    B->p=B;

    *root=B;
}

void del_tree(AVL **root)
{
    if(*root!=NULL)
    {
        del_tree(&(*root)->l);
        del_tree(&(*root)->r);
        free(*root);
    }
}

int height (AVL *root)
{
    if(!root)
        return 0;
    if(!root->l && !root->r)
        return 0;
    
    int lh=0,rh=0;
    if(root->l)
    lh=height(root->l);
    if(root->r)
    rh=height(root->r);

    if(lh>=rh)
        return lh+1;
    else
        return rh+1;
}

int bal_fac(AVL *root)
{
    return (height(root->l)-height(root->r));
}

void main()
{
    int data;
    printf("Enter the data of the root node: ");
    scanf(" %d",&data);
    AVL *root=new_node(&root,data);

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
                int n=5;
                int arr[]={6,2,8,15,1};
                int i;
                for (i=0;i<n;i++)
                {
                    //printf("%d\n",__LINE__);
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
                Left_rotate(&root);
                break;
            }
            case 5:
            {
                Right_rotate(&root);
                break;
            }
            case 6:
            {
                int n=2;
                int arr[]={6,2,8,15,1};
                int i;
                for (i=0;i<n;i++)
                {
                    printf("%d %d\n",(root)->data,__LINE__);
                    add_node_avl(&root,arr[i]);
                }
                break;
            }
            case 7:
            {
                AVL **node=&root;
                AVL *ptr=*node;
                printf("%d\n",bal_fac(root));
                printf("%d\n",bal_fac(*node));
                printf("%d\n",bal_fac(ptr));
                break;
            }
            case 8:
            {
                del_tree(&root);
                printf("Enter the data of the root node: ");
                scanf(" %d",&data);
                root=new_node(&root,data);
                break;
            }
        }
    } while (ch!=0);
    
}
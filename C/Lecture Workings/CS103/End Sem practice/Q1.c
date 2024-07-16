#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

typedef struct node
{
    struct node *l,*p,*r;
    int data;
}Tree;

Tree *par=NULL;
Tree *Par=NULL;
Tree *new_node(Tree **parent,int data)
{
    Tree *node=(Tree *)calloc(1,sizeof(Tree));
    node->l=NULL;
    node->r=NULL;
    node->p=*parent;
    node->data=data;
    
    return node;
}

void add_node_bt(Tree **node,int data)
{
    if(*node==NULL)
    {
        *node=new_node(&par,data);
        return;
    }
    if((rand()%4)-2>=0)
    {
        if(!(*node)->l)
            par=*node;
        add_node_bt(&(*node)->l,data);
    }
    else
    {
        if(!(*node)->r)
            par=*node;
        add_node_bt(&(*node)->r,data);
    }
}

void add_node_bst(Tree **node, int data) {
    if (*node == NULL) {
        *node = new_node(&Par, data);
        return;
    }
    if (data <= (*node)->data) {
        if (!(*node)->l)
            Par = *node; // Update Par when adding left child
        add_node_bst(&(*node)->l, data);
    } else {
        if (!(*node)->r)
            Par = *node; // Update Par when adding right child
        add_node_bst(&(*node)->r, data);
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

int is_bst(Tree *root)
{
    if(!root)
    {
        printf("%d\n",__LINE__);
        return 1;
    }
        
    if(!root->l && !root->r)
    {
        printf("%d\n",__LINE__);
        return 1;
    }
        
    if(root->l && root->r)
    {
        if(root->l->data<=root->data && root->r->data>root->data && is_bst(root->l) && is_bst(root->r))
        {
            printf("%d\n",__LINE__);
            return 1;
        }
    }

    else if(root->l)
    {
         if(root->l->data<=root->data && is_bst(root->l))
         {
            printf("%d\n",__LINE__);
            return 1;
         }
    }
        
    else if(root->r)
    {
         if(root->l->data<=root->data && is_bst(root->l))
         {
            printf("%d\n",__LINE__);
            return 1;
         }
    }
    
    else 
    {
        printf("%d\n",__LINE__);
         return 0;
    }
       
}

/*
int is_bst(Tree *root)
{
    if (!root)
        return 1;
    
    if (root->l && (root->l->data >= root->data))
        return 0;
    
    if (root->r && (root->r->data <= root->data))
        return 0;
    
    if (!is_bst(root->l) || !is_bst(root->r))
        return 0;
    
    return 1;
}
*/
void spaces(int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf(" ");
    }
}

void draw_tree_hori(Tree *root,int sp)
{
    if(!root)
        return;
    
    sp+=5;

    draw_tree_hori(root->r,sp);

    printf("\n");
    spaces(sp);
    printf("%d\n",root->data);

    draw_tree_hori(root->l,sp);
}

void draw_tree(Tree *root)
{
    draw_tree_hori(root,0);
}

void main()
{
    int data;
    printf("Enter the data for the root node: ");
    scanf(" %d",&data);
    Tree *root=new_node(&par,data);
    Tree *Root=new_node(&Par,data);
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                printf("In order representation of bt: \n");
                in_order(root);
                printf("\n");

                printf("In order representation of bst: \n");
                in_order(Root);
                printf("\n");

                break;
            }
            case 2:
            {
                int n=7;
                int arr[]={17,-5,28,1,-3,54,81};
                int i;
                for (i=0;i<n;i++)
                {
                    printf("%d\n",__LINE__);
                    add_node_bt(&root,arr[i]);
                }

                for (i=0;i<n;i++)
                {
                    printf("%d\n",__LINE__);
                    add_node_bst(&Root,arr[i]);
                }
                break;
            }
            case 3:
            {
                printf("%d\n",__LINE__);
                is_bst(root);
                printf("%d\n",__LINE__);
                if(is_bst(root))
                    printf("bt Is BST\n");
                else
                    printf("bt Not a BST\n");

                is_bst(Root);
                printf("%d\n",__LINE__);
                if(is_bst(Root))
                    printf("bst Is BST\n");
                else
                    printf("bst Not a BST\n");
                break;
            }
            case 4:
            {
                printf("Bt: \n");
                draw_tree(root);
                printf("\n");

                printf("Bst: \n");
                draw_tree(Root);
                printf("\n");
                
                break;
            }
        }
    }while(ch!=0);
}
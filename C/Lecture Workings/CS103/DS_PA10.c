#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

typedef struct tree
{
    struct tree *p,*l,*r;
    int data;
}Tree;

Tree *new_node(Tree **parent,int data)
{
    Tree *node=(Tree *)calloc(1,sizeof(Tree));
    node->data=data;
    node->p=*parent;
    node->l=NULL;
    node->r=NULL;

    return node;
}

Tree *par=NULL;
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

void pre_order(Tree *root)
{
    if(root)
    {
        printf("%d ",root->data);
        pre_order(root->l);
        pre_order(root->r);
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

void post_order(Tree *root)
{
    if(root)
    {
        post_order(root->l);
        post_order(root->r);
        printf("%d ",root->data);
    }
}

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

Tree *get_node(Tree *root,int data)
{
    //printf("%d\n",__LINE__);
    Tree *node;
    if(!root)
    {
        return NULL;
    } 
    if(root->data==data)
    {
        //printf("%d\n",__LINE__);
        return root;
    }
    
        //printf("%d\n",__LINE__);
        node=get_node(root->l,data);
        if (node) 
        {
            //printf("%d\n",__LINE__);
            return node; 
        }
    
        //printf("%d\n",__LINE__);
        node=get_node(root->r,data);
        if (node) 
        {
            //printf("%d\n",__LINE__);
            return node; 
        }
    
    //printf("%d\n",__LINE__);
    return NULL;
}

void mirror(Tree **root)
{
    if(*root)
    {
        Tree *temp=(*root)->l;
        (*root)->l=(*root)->r;
        (*root)->r=temp;

        mirror(&(*root)->l);
        mirror(&(*root)->r);
    }
}

void clone_bt(Tree *root,Tree **node)
{
    if(!root)
    {
        *node=new_node(node,root->data);
        return;
    }
    
    if(root->l)
    {
        (*node)->l=new_node(node,root->l->data);
        clone_bt(root->l,&(*node)->l);
    }
    if(root->r)
    {
        (*node)->r=new_node(node,root->r->data);
        clone_bt(root->r,&(*node)->r);
    }
}

int comp(int m,int n)
{
    return m == n ? 1 : 0;
}

void key_comp(Tree *r1,Tree *r2)
{
    if (r1 && r2)
    {
        if(comp(r1->data,r2->data))
            printf("Same\n");
        else
            printf("Diff\n");
        
        key_comp(r1->l,r2->l);
        key_comp(r1->r,r2->r);
    }
    else
        printf("diff str\n");
}

void del_bt(Tree **root)
{
    if(*root)
    {
        del_bt(&(*root)->l);
        del_bt(&(*root)->r);
        free(*root);
    }
}

void num_leaf_nodes(Tree *root,int *c)
{
    if(!root->l && !root->r)
    {
        (*c)++;
    }
    if(root->l)
    num_leaf_nodes(root->l,c);
    if(root->r)
    num_leaf_nodes(root->r,c);
}

void num_int_nodes(Tree *root,int *c)
{
    if(!root->l && !root->r)
    {
        return;
    }
    else
    {
        (*c)++;
        if(root->l)
            num_int_nodes(root->l,c);
        if(root->r)
            num_int_nodes(root->r,c);
    }
}

void in_order_leaf_nodes(Tree *root)
{
    if(root)
    {
        in_order_leaf_nodes(root->l);
        if(!root->l && !root->r)
            printf("%d ",root->data);
        in_order_leaf_nodes(root->r);
    }
}

void in_order_int_nodes(Tree *root)
{
    if(root)
    {
        in_order_int_nodes(root->l);
        if(!(!root->l && !root->r))
            printf("%d ",root->data);
        in_order_int_nodes(root->r);
    }
}

Tree *in_order_pre(Tree *node)
{
    node=node->l;
    if(node)
    {
        while(node->r)
        {
        printf("%d\n",__LINE__);
        node=node->r;
        }
    }
   
   return node;
}

Tree *in_order_suc(Tree *node)
{
    node=node->r;
    if(node)
    {
        while(node->l)
        {
        printf("%d\n",__LINE__);
        node=node->l;
        }
    }
   
   return node;
    
}

Tree *IO_pre(Tree *root,int data)
{
    Tree *node=get_node(root,data);
    //if(node)
    return in_order_pre(node);
}

Tree *IO_suc(Tree *root,int data)
{
    printf("%d\n",__LINE__);
    Tree *node=get_node(root,data);
    //if(node)
    printf("%d\n",__LINE__);
    return in_order_suc(node);
}

int height (Tree *root)
{
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

int height_node(Tree *root,int data)
{
    return height(get_node(root,data));
}

int depth_node(Tree *root,int data)
{
    Tree *node=get_node(root,data);

    int c=0;
    while(node!=root)
    {
        c++;
        node=node->p;
    }
    return c;
}

void main()
{
    int data;
    printf("Enter the data of the parent node: ");
    scanf(" %d",&data);

    Tree *root=new_node(&root,data);
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch (ch)
        {
        case 1:
        {
            printf("Pre order:\n");
            pre_order(root);
            printf("\n");
            break;
        }
        case 2:
        {
            printf("In order:\n");
            in_order(root);
            printf("\n");
            break;
        }
        case 3:
        {
            printf("Post order:\n");
            post_order(root);
            printf("\n");
            break;
        }
        case 4:
        {
            int n=9;
            int arr[]={12,0,-17,54,30,61,-31,73,42,81,7};
            int i;
            for (i=0;i<n;i++)
            {
                add_node_bt(&root,arr[i]);
            }
            break;
        }
        case 5:
        {
            draw_tree(root);
            break;
        }
        case 6:
        {
            int data;
            printf("Enter the data to be fetched: ");
            scanf(" %d",&data);
            Tree *node=get_node(root,data);
            if(node)
                printf("The node found has data = %d\n",node->data);
            else
                printf("Data not found.\n");
            break;
        }
        case 7:
        {
            mirror(&root);
            break;
        }
        case 8:
        {
            Tree *Root=new_node(&Root,root->data);
            clone_bt(root,&Root);

            printf("In Order of clone:\n");
            in_order(Root);
            printf("\n");

            break;
        }
        case 9:
        {
            int data;
            printf("Enter the data of parent node 2nd tree: ");
            scanf(" %d",&data);
            Tree *Root=new_node(&Root,data);

            int n=9;
            int arr[]={12,0,-27,54,30,67,-31,83,42,81,7};
            int i;
            for (i=0;i<n;i++)
            {
                add_node_bt(&Root,arr[i]);
            }

            draw_tree(Root);

            key_comp(root,Root);

            break;
        }
        case 10:
        {
            del_bt(&root);
            break;
        }
        case 11:
        {
            int cnt=0;
            int *c=&cnt;

            num_leaf_nodes(root,c);
            printf("Number of leaf nodes = %d\n",*c);
            break;
        }
        case 12:
        {
            int cnt=0;
            int *c=&cnt;
            num_int_nodes(root,c);

            printf("Number of internal nodes = %d\n",*c);
            break;
        }
        case 13:
        {
            printf("In order representation of leaf nodes:\n");
            in_order_leaf_nodes(root);
            printf("\n");
            break;
        }
        case 14:
        {
            printf("In order representation of non leaf nodes:\n");
            in_order_int_nodes(root);
            printf("\n");
            break;
        }
        case 15:
        {
            int data;
            printf("Enter the data of the node whose IO pre is to be found: ");
            scanf(" %d",&data);
            Tree *node=IO_pre(root,data);
            if(node)
            {
                printf("In order of node: \n");
                in_order(get_node(root,data));
                printf("\n");
                printf("The IO pre of %d is %d\n",get_node(root,data)->data,node->data);
            }
            else
                printf("Does not exist\n");
            break;
        }
        case 16:
        {
            int data;
            printf("Enter the data of the node whose IO suc is to be found: ");
            scanf(" %d",&data);
            printf("%d\n",__LINE__);
            Tree *node=IO_suc(root,data);
            printf("%d\n",__LINE__);
            if(node)
            {
                printf("%d\n",__LINE__);
                printf("In order of node: \n");
                in_order(get_node(root,data));
                printf("\n");
                printf("The IO suc of %d is %d\n",get_node(root,data)->data,node->data);
            }
            printf("%d\n",__LINE__);
            if(!node)
            {
                printf("%d\n",__LINE__);
                printf("Does not exist\n");
            }
                
            break;
        }
        case 17:
        {
            printf("Height of the tree = %d\n",height(root));
            break;
        }
        case 18:
        {
            int data;
            printf("Enter the data whose node height is to be found: ");
            scanf(" %d",&data);

            printf("The height of the node(=%d) = %d\n",data,height_node(root,data));
            break;
        }
        case 19:
        {
            int data;
            printf("Enter the data whose node depth is to be found: ");
            scanf(" %d",&data);
            printf("The depth of node(=%d) = %d\n",data,depth_node(root,data));
            break;
        }
        }
    } while (ch!=0);
    
}
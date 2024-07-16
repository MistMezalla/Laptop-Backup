#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

typedef struct tree
{
    struct tree *l,*p,*r;
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
void add_node_bst(Tree **node,int data)
{
    if (*node == NULL)
    {
        *node=new_node(&par,data);
        return;
    }
    else if(data<=(*node)->data)
    {
        if(!(*node)->l)
            par=*node;
        add_node_bst(&(*node)->l,data);
    }
    else if(data>(*node)->data)
    {
        if(!(*node)->r)
            par=*node;
        add_node_bst(&(*node)->r,data);
    }
}

void add_node_bst_iter(Tree **root,int data)
{
    Tree *ptr,*preptr;

    ptr=preptr=*root;

    while(ptr!=NULL)
    {
        preptr=ptr;
        if(data<=ptr->data)
            ptr=ptr->l;
        else
            ptr=ptr->r;
    }

    if(data<=preptr->data)
    {
        preptr->l=new_node(&preptr,data);
    }
    else
    {
        preptr->r=new_node(&preptr,data);
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
    for (i=0;i<n;i++)
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
    if(!root)
    {
        printf("Data not found\n");
        return NULL;
    }
    if(root && root->data==data)
    {
        return root;
    }
    if(data <= root->data)
    {
        get_node(root->l,data);
    }
    else if(data > root->data)
    {
        get_node(root->r,data);
    }
}

Tree *NLR_pre(Tree *root)
{
    while(root->r)
    {
        root=root->r;
    }
    return root;
}
/*
void del_node(Tree **node,int data)
{
    printf("%d\n",__LINE__);
    if(*node==NULL)
    {
        printf("%d\n",__LINE__);
        printf("Data not found\n");
        return;
    }
    if(data<(*node)->data)
    {
        printf("%d\n",__LINE__);
        del_node(&(*node)->l,data);
    }
    else if(data>(*node)->data)
    {
        printf("%d\n",__LINE__);
        del_node(&(*node)->r,data);
    }
    if((*node)->l && (*node)->r)
    {
        printf("%d\n",__LINE__);
        Tree *temp=NLR_pre((*node)->l);
        printf("%d\n",__LINE__);
        (*node)->data=temp->data;
        del_node(&(*node)->l,temp->data);
    }
    else
    {
        printf("%d\n",__LINE__);
        if(!(*node)->l && !(*node)->r)
        {
            printf("%d\n",__LINE__);
            (*node)->p->l=(*node)->p->r=NULL;
            free(*node);
            return;
        }
        else if((*node)->r!=NULL)
        {
            //printf("%d\n",__LINE__);
            (*node)->r->p=(*node)->p;
            if((*node)->p->r==*node)
                (*node)->p->r=(*node)->r;
            else if((*node)->p->l==*node)
                (*node)->p->l=(*node)->r;
            free(*node);
        }
        else if((*node)->l!=NULL)
        {
            //printf("%d\n",__LINE__);
             (*node)->l->p=(*node)->p;
            if((*node)->p->r==*node)
                (*node)->p->r=(*node)->l;
            else if((*node)->p->l==*node)
                (*node)->p->l=(*node)->l;
        }
    }
        
}
*/
void del_node(Tree **root,int data)
{
    Tree *node=*root;
    printf("%d\n",__LINE__);
    if(node==NULL)
    {
        printf("%d\n",__LINE__);
        printf("Data not found\n");
        return;
    }
    else if(data<node->data)
    {
        printf("%d\n",__LINE__);
        del_node(&node->l,data);
    }
    else if(data>node->data)
    {
        printf("%d\n",__LINE__);
        del_node(&node->r,data);
    }
    else if(node->l && node->r)
    {
        printf("%d\n",__LINE__);
        Tree *temp=NLR_pre(node->l);
        node->data=temp->data;
        del_node(&node->l,temp->data);
    }
    else
    {
        printf("%d\n",__LINE__);
        if(!node->l && !node->r)
        {
            printf("%d\n",node->p->data);
            printf("%d\n",__LINE__);
            if(node->p->l==node)
            {
                node->p->l=NULL;
                printf("%d\n",__LINE__);
            }
            else
            {
                node->p->r=NULL;
                printf("%d\n",__LINE__);
            }
            
        free(node);
        return;
        }
        else if(node->r!=NULL)
        {
            printf("%d\n",__LINE__);
            node->r->p=node->p;
            if(node->p->r==node)
                node->p->r=node->r;
            else if(node->p->l==node)
                node->p->l=node->r;
            free(node);
        }
        else if(node->l!=NULL)
        {
            printf("%d\n",__LINE__);
             node->l->p=node->p;
            if(node->p->r==node)
                node->p->r=node->l;
            else if(node->p->l==node)
                node->p->l=node->l;
            free(node);
        }
    }
}

void del_tree(Tree **root)
{
    if(*root)
    {
        del_tree(&(*root)->l);
        del_tree(&(*root)->r);
        free(*root);
    }
}

Tree *min_bst(Tree *root)
{
    if(root && !root->l)
    {
        return root;
    }
    else 
    {
        min_bst(root->l);
    }
}

Tree *max_bst(Tree *root)
{
    if(root && !root->r)
    {
        return root;
    }
    else
    {
        max_bst(root->r);
    }
}

void add_node_bt(Tree **root,int data)
{
    if(*root==NULL)
    {
        *root=new_node(&par,data);
        return;
    }
    if((rand()%4)-2>=0)
    {
        if((*root)->l==NULL)
        {
           par=*root;
        }
        add_node_bt(&(*root)->l,data);
    }
    else
    {
        if((*root)->r==NULL)
        {
           par=*root;
        }
        add_node_bt(&(*root)->r,data);
    }
}

int is_bst(Tree *root)
{
    if(!root)
    {
        return 1;
    }
    else if(!root->l && !root->r)
        return 1;

    else if (root->l && root->r)
    {
        is_bst(root->l);
        is_bst(root->r);
        if(root->l->data<=root->data && root->r->data>root->data && is_bst(root->l) && is_bst(root->r))
            return 1;
    }
    else if(root->l)
    {
        if(root->l->data<=root->data && is_bst(root->l))
            return 1;
        return 0;
    }
    else if(root->r)
    {
        if(root->r->data>root->data && is_bst(root->r))
            return 1;
        return 0;
    }
    return 0;
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
    else
    {
        return;
    }
}

Tree *min_bt(Tree *root)
{
    Tree *min=NULL;

    if(root)
    {
        min=root;
        
        Tree *min_left=min_bt(root->l);
        Tree *min_right=min_bt(root->r);
        
        if(min_left && min_left->data<=min->data)
            min=min_left;
        if(min_right && min_right->data<=min->data)
            min=min_right;
    }
    return min;
}

Tree *max_bt(Tree *root)
{
    Tree *max=NULL;

    if(root)
    {
        max=root;

        Tree *max_l=max_bt(root->l);
        Tree *max_r=max_bt(root->r);

        if(max_l && max_l->data>=max->data)
            max=max_l;
        if(max_r && max_r->data>=max->data)
            max=max->r;
    }
    return max;
}

void clone_tree(Tree *root,Tree **node)
{
    if (!root)
        return;
    
    if(root->l)
    {
        (*node)->l=new_node(&(*node),root->l->data);
        clone_tree(root->l,(&(*node)->l));
    }
    if(root->r)
    {
        (*node)->r=new_node(&(*node),root->r->data);
        clone_tree(root->r,(&(*node)->r));
    }
}

int are_identical(Tree *r1,Tree *r2)
{
    if(!r1 && !r2)
    {
        return 1;
    }
    if(!r1 || !r2)
    {
        return 0;
    }
    return (are_identical(r1->l,r2->l) && are_identical(r1->r,r2->r));
}

void num_nodes(Tree *root,int *c)
{
    if(root)
    {
        num_nodes(root->l,c);
        num_nodes(root->r,c);
        (*c)++;
    }
}

void num_int_nodes(Tree *root,int *c)
{
    if(!root)
    {
        return;
    }
    if (root->l || root->r)
    {
        (*c)++;
        num_int_nodes(root->l,c);
        num_int_nodes(root->r,c);
    }
}

void num_ext_nodes(Tree *root,int *c)
{
    if(!root)
    {
        return;
    }
    if(!root->l && !root->r)
    {
        (*c)++;
    }
    else
    {
        num_ext_nodes(root->l,c);
        num_ext_nodes(root->r,c);
    }
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

        switch(ch)
        {
            case 1:
            {
                int n=9;
                int arr[]={27,84,0,-13,7,-29,64,36,80};
                
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bst(&root,arr[i]);
                }
                break;
            }
            case 2:
            {
                int n=9;
                int arr[]={27,84,0,-13,7,-29,64,36,80};
                
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bst_iter(&root,arr[i]);
                }
                break;
            }
            case 3:
            {
                printf("Pre Order: \n");
                pre_order(root);
                printf("\n");
                break;
            }
            case 4:
            {
                printf("In Order: \n");
                in_order(root);
                printf("\n");
                break;
            }
            case 5:
            {
                printf("Post Order: \n");
                post_order(root);
                printf("\n");
                break;
            }
            case 6:
            {
                draw_tree(root);
                break;
            }
            case 7:
            {
                int data;
                printf("Enter the data to be fetched: ");
                scanf(" %d",&data);
                Tree *node=get_node(root,data);
                printf("The data fetched = %d\n",node->data);
                break;
            }
            case 8:
            {
                int data;
                printf("Enter the data to be deleted: ");
                scanf(" %d",&data);
                del_node(&root,data);
                printf("%d\n",__LINE__);
                break;
            }
            case 9:
            {
                del_tree(&root);
                root=NULL;
                break;
            }
            case 10:
            {
                Tree *node=min_bst(root);
                printf("Smallest in bst = %d\n",node->data);
                break;
            }
            case 11:
            {
                Tree *node=max_bst(root);
                printf("Largest in bst = %d\n",node->data);
                break;
            }
            case 12:
            {
                int n=9;
                int arr[]={27,84,0,-13,7,-29,64,36,80};
                
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bt(&root,arr[i]);
                }
                break;
            }
            case 13:
            {
                if(is_bst(root))
                    printf("Tree is bst\n");
                else 
                    printf("Tree is not bst\n");
                break;
            }
            case 14:
            {
                mirror(&root);
                break;
            }
            case 15:
            {
                Tree *node=min_bt(root);
                printf("Min of bt = %d\n",node->data);
                break;
            }
            case 16:
            {
                Tree *node=max_bt(root);
                printf("Max of bt = %d\n",node->data);
                break;
            }
            case 17:
            {
                Tree *clone_root=new_node(&clone_root,root->data);
                clone_tree(root,&clone_root);
                printf("In order of clone: \n");
                in_order(clone_root);
                printf("\n");
                draw_tree(clone_root);
                break;
            } 
            case 18:
            {
                Tree *Root=new_node(&Root,root->data);

                int n=9;
                int arr[]={27,84,0,-13,7,-29,64,36,80};
                
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bt(&Root,arr[i]);
                }
                
                if(are_identical(Root,root))
                    printf("Identical\n");
                else   
                    printf("Not identical\n");
                    break;
            }
            case 19:
            {
                int *c;
                int count=0;
                c=&count;
                
                num_nodes(root,c);
                printf("Num of nodes = %d\n",*c);
                break;
            }
            case 20:
            {
                int *c;
                int count=0;
                c=&count;

                num_int_nodes(root,c);
                printf("Internal nodes = %d\n",*c);
                break;
            }
            case 21:
            {
                int *c;
                int count=0;
                c=&count;

                num_ext_nodes(root,c);
                printf("External nodes = %d\n",*c);
                break;
            }
        }
    } while(ch!=0);   
}

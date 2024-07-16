#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *l, *p, *r;
} AVL;

AVL *new_node(AVL **parent, int data)
{
    AVL *node = (AVL *)calloc(1, sizeof(AVL));

    node->data = data;
    node->l = NULL;
    node->r = NULL;
    node->p = *parent;

    return node;
}

AVL *par = NULL;

void add_node_avl(AVL **root, int data);

void add_node_bst(AVL **root, int data)
{
    if (!(*root))
    {
        if (par)
            printf("Parent: %d\n", par->data);
        *root = new_node(&par, data);
        add_node_avl(root, data); // After adding node, balance the AVL
        par = NULL; // Reset par to NULL after insertion
        return;
    }
    if (data <= (*root)->data)
    {
        if (!(*root)->l)
        {
            par = *root;
        }
        add_node_bst(&(*root)->l, data);
    }
    else
    {
        if (!(*root)->r)
        {
            par = *root;
        }
        add_node_bst(&(*root)->r, data);
    }
}

void in_order(AVL *root)
{
    if (root)
    {
        in_order(root->l);
        printf("%d ", root->data);
        in_order(root->r);
    }
}

void spaces(int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf(" ");
    }
}

void AVL_hori(AVL *root, int sp)
{
    if (!root)
        return;

    sp += 5;

    AVL_hori(root->r, sp);

    printf("\n");
    spaces(sp);
    printf("%d\n", root->data);

    AVL_hori(root->l, sp);
}

void draw_AVL(AVL *root)
{
    AVL_hori(root, 0);
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

void del_AVL(AVL **root)
{
    if (*root != NULL)
    {
        del_AVL(&(*root)->l);
        del_AVL(&(*root)->r);
        free(*root);
    }
}

int height(AVL *root)
{
    if (!root)
        return 0;
    if (!root->l && !root->r)
        return 0;

    int lh = 0, rh = 0;
    if (root->l)
        lh = height(root->l);
    if (root->r)
        rh = height(root->r);

    if (lh >= rh)
        return lh + 1;
    else
        return rh + 1;
}

int bal_fac(AVL *root)
{
    return (height(root->l) - height(root->r));
}

void balance_AVL(AVL **root);

void add_node_avl(AVL **root, int data)
{
    add_node_bst(root, data); // Add the node to the BST
    balance_AVL(root);       // Balance the AVL after adding the node
}

void del_node(AVL **root,int data)
{
    AVL *node=*root;
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
        AVL *temp=NLR_pre(node->l);
        printf("%d\n",__LINE__);
        node->data=temp->data;
        del_node(&node->l,temp->data);
    }
    else
    {
        printf("%d\n",__LINE__);
        if(!node->l && !node->r)
        {
            printf("%d\n",__LINE__);
            if(node->p->r==node)
                node->p->r=NULL;
            else if(node->p->l==node)
                node->p->l=NULL;
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
        }
        else if(node->l!=NULL)
        {
            printf("%d\n",__LINE__);
             node->l->p=node->p;
            if(node->p->r==node)
                node->p->r=node->l;
            else if(node->p->l==node)
                node->p->l=node->l;
        }
    }
    balance_AVL(root);
}

void balance_AVL(AVL **root)
{
    if (!(*root))
        return;

    balance_AVL(&(*root)->l);
    balance_AVL(&(*root)->r);

    int balance = bal_fac(*root);

    if (balance > 1) // Left heavy
    {
        if (bal_fac((*root)->l) >= 0) // Left-Left case
            Right_rotate(root);
        else // Left-Right case
        {
            Left_rotate(&(*root)->l);
            Right_rotate(root);
        }
    }
    else if (balance < -1) // Right heavy
    {
        if (bal_fac((*root)->r) <= 0) // Right-Right case
            Left_rotate(root);
        else // Right-Left case
        {
            Right_rotate(&(*root)->r);
            Left_rotate(root);
        }
    }
}

void main()
{
    int data;
    printf("Enter the data of the root node: ");
    scanf(" %d", &data);
    AVL *root = new_node(&root, data);

    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d", &ch);
        switch (ch)
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
            int n = 5;
            int arr[] = {6, 2, 8, 15, 1};
            int i;
            for (i = 0; i < n; i++)
            {
                add_node_bst(&root, arr[i]);
            }
            break;
        }
        case 3:
        {
            draw_AVL(root);
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
            int n = 2;
            int arr[] = {6, 2, 8, 15, 1};
            int i;
            for (i = 0; i < n; i++)
            {
                add_node_bst(&root, arr[i]);
            }
            break;
        }
        case 7:
        {
            AVL **node = &root;
            AVL *ptr = *node;
            printf("%d\n", bal_fac(root));
            printf("%d\n", bal_fac(*node));
            printf("%d\n", bal_fac(ptr));
            break;
        }
        case 8:
        {
            del_AVL(&root);
            printf("Enter the data of the root node: ");
            scanf(" %d", &data);
            root = new_node(&root, data);
            break;
        }
        case 9:
        {
            int data;
            printf("Enter the data to be deleted: ");
            scanf(" %d",&data);
            del_node(&root,data);
            break;
        }
        }
    } while (ch != 0);
}

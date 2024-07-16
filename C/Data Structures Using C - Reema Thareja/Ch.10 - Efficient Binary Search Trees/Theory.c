#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

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

Tree *par=NULL;
void add_node(Tree **node,int data)
{
    if(*node==NULL)
   {
    *node=new_node(&par,data);
    return;
   }
    if(data<=(*node)->data)
    {
        if((*node)->l==NULL)
        {
           par=*node;
        }
        add_node(&(*node)->l,data);
    }
    else
    {
        if((*node)->r==NULL)
        {
           par=*node;
        }
        add_node(&(*node)->r,data);
    }
}

void add_node_iterative(Tree **root,int data)
{
    Tree *ptr=*root;
    Tree *preptr;
    //printf("%d\n",__LINE__);
    while(ptr!=NULL)
    {
        //printf("%d\n",__LINE__);
        preptr=ptr;
        if(data<=ptr->data)
        {
            //printf("%d\n",__LINE__);
            ptr=ptr->l;
        }
        else if(data>ptr->data)
        {
            //printf("%d\n",__LINE__);
            ptr=ptr->r;
        }
    }
    //printf("%d\n",__LINE__);
    if(data<=preptr->data)
    {
        preptr->l=new_node(&preptr,data);
    }
    else if(data>preptr->data)
    {
        preptr->r=new_node(&preptr,data);
    }
    //printf("\n%d\t%d\n",preptr->l,preptr->r);
    //printf("\n%d\t%d\n",ptr->p->data,ptr->data);
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

Tree *get_node(Tree *root,int data)
{
    //printf("%d\n",__LINE__);
    if (root==NULL || root->data==data)
    {
        //printf("%d\n",__LINE__);
        return root;
    }
    else if(root->data>=data)
    {
        //printf("%d\n",__LINE__);
        get_node(root->l,data);
    }
    else if(root->data<data)
    {
        //printf("%d\n",__LINE__);
        get_node(root->r,data);
    }
}

Tree *NLR_pre(Tree *node)
{
    //printf("%d\n",__LINE__);
    while(node->r!=NULL)
    {
        //printf("%d\n",__LINE__);
        node=node->r;
    }
    return node;
}

void del_node(Tree **root,int data)
{
    Tree *node=*root;
    //printf("%d\n",__LINE__);
    if(node==NULL)
    {
        //printf("%d\n",__LINE__);
        printf("Data not found\n");
        return;
    }
    else if(data<node->data)
    {
        //printf("%d\n",__LINE__);
        del_node(&node->l,data);
    }
    else if(data>node->data)
    {
        //printf("%d\n",__LINE__);
        del_node(&node->r,data);
    }
    else if(node->l && node->r)
    {
        //printf("%d\n",__LINE__);
        Tree *temp=NLR_pre(node->l);
        node->data=temp->data;
        del_node(&node->l,temp->data);
    }
    else
    {
        //printf("%d\n",__LINE__);
        if(!node->l && !node->r)
        {
            //printf("%d\n",__LINE__);
            node->p->r=node->p->l=NULL;
        free(node);
        return;
        }
        else if(node->r!=NULL)
        {
            //printf("%d\n",__LINE__);
            node->r->p=node->p;
            if(node->p->r==node)
                node->p->r=node->r;
            else if(node->p->l==node)
                node->p->l=node->r;
        }
        else if(node->l!=NULL)
        {
            //printf("%d\n",__LINE__);
             node->l->p=node->p;
            if(node->p->r==node)
                node->p->r=node->l;
            else if(node->p->l==node)
                node->p->l=node->l;
        }
    }
}

void del_tree(Tree **root)
{
    if(*root!=NULL)
    {
        del_tree(&(*root)->l);
        del_tree(&(*root)->r);
        free(*root);
    }
}

Tree *smallest(Tree *root)
{
    if(root!=NULL && root->l==NULL)
    {
        return root;
    }
    else
    {
        smallest(root->l);
    }
}

Tree *largest(Tree *root)
{
    if(root!=NULL && root->r==NULL)
    {
        return root;
    }
    else
    {
        largest(root->r);
    }
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
        if((*node)->l==NULL)
        {
           par=*node;
        }
        add_node(&(*node)->l,data);
    }
    else
    {
        if((*node)->r==NULL)
        {
           par=*node;
        }
        add_node(&(*node)->r,data);
    }
}
/*
Tree *min_node_bt(Tree *root,int *min)
{
    printf("%d\n",__LINE__);
    *min=root->data;
    if (*root==NULL)
    {
        printf("%d\n",__LINE__);
        printf("Invalid\n");
    }

    if(!root->l && root->r)
    {
        printf("%d\n",__LINE__);
        if(root->data<=*min)
        printf("%d\n",__LINE__);
            *min=root->data;
    }
    if((*root)->l && (*root)->l->data <= (*min)->data)
    {
        *min=(*root)->l;
        if((*root)->l)
            min_node_bt(&(*root)->l);
    }
    if((*root)->r && (*root)->r->data <= (*min)->data)
    {
        printf("%d\n",__LINE__);
        *min=(*root)->r;
        if((*root)->r)
        printf("%d\n",__LINE__);
            min_node_bt(&(*root)->r);
    }
    printf("%d\n",__LINE__);
    return *min;
}

Tree *max_node_bt(Tree *node)
{
    Tree **max=node;
    if (node==NULL)
        printf("Invalid\n");
    if(!node->l && !node->r)
    {
        if(node->data<=(*max)->data)
            *max=node;
    }
    if(node->l && node->l->data <= (*max)->data)
    {
        *max=node->l;
        if(node->l)
            max_node_bt(node->l);
    }
    if(node->r && node->r->data <= (*max)->data)
    {
        *max=node->r;
        if(node->r)
            max_node_bt(node->r);
    }
    return *max;
}
*/
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

void mirror_img(Tree **node)
{
    if(*node!=NULL)
    {
        Tree *temp=(*node)->l;
        (*node)->l=(*node)->r;
        (*node)->r=temp;
        mirror_img(&(*node)->l);
        mirror_img(&(*node)->r);
    }
    else
        return;
}

int _print_t(Tree *tree, int is_left, int offset, int depth, char s[20][255])
{
    char b[20];
    int width = 5;

    if (!tree) return 0;

    sprintf(b, "(%03d)", tree->data);

    int left  = _print_t(tree->l,  1, offset,                depth + 1, s);
    int right = _print_t(tree->r, 0, offset + left + width, depth + 1, s);

#ifdef COMPACT
    for (int i = 0; i < width; i++)
        s[depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (int i = 0; i < width + right; i++)
            s[depth - 1][offset + left + width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';

    } else if (depth && !is_left) {

        for (int i = 0; i < left + width; i++)
            s[depth - 1][offset - width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';
    }
#else
    for (int i = 0; i < width; i++)
        s[2 * depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (int i = 0; i < width + right; i++)
            s[2 * depth - 1][offset + left + width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset + left + width + right + width/2] = '+';

    } else if (depth && !is_left) {

        for (int i = 0; i < left + width; i++)
            s[2 * depth - 1][offset - width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset - width/2 - 1] = '+';
    }
#endif

    return left + width + right;
}

void print_tree(Tree *tree)
{
    char s[20][255];
    for (int i = 0; i < 20; i++)
        sprintf(s[i], "%80s", " ");

    _print_t(tree, 0, 0, 0, s);

    for (int i = 0; i < 20; i++)
        printf("%s\n",s[i]);
}

void printSpaces(int n) {
    for (int i = 0; i < n; i++)
        printf(" ");
}

// Function to draw a binary tree
void drawTreeUtil(Tree *root, int space) {
    // Base case
    if (root == NULL)
        return;

    // Increase distance between levels
    space += 5;

    // Process right child first
    drawTreeUtil(root->r, space);

    // Print current node after space
    printf("\n");
    printSpaces(space);
    printf("%d\n", root->data);

    // Process left child
    drawTreeUtil(root->l, space);
}

// Function to draw a binary tree
void drawTree(Tree *root) //downward (RNL) printing
{
    // Start with space as 0
    drawTreeUtil(root, 0);
}

Tree *find_min_node(Tree *root) 
{
    Tree *min_node = NULL;
    if (root != NULL) 
    {
        min_node = root;
        Tree *left_min = find_min_node(root->l);
        Tree *right_min = find_min_node(root->r);
        if (left_min != NULL && left_min->data < min_node->data)
            min_node = left_min;
        if (right_min != NULL && right_min->data < min_node->data)
            min_node = right_min;
    }
    return min_node;
}

Tree *find_max_node(Tree *root) 
{
    Tree *max_node = NULL;
    if (root != NULL) 
    {
        max_node = root;
        Tree *left_max = find_max_node(root->l);
        Tree *right_max = find_max_node(root->r);
        if (left_max != NULL && left_max->data > max_node->data)
            max_node = left_max;
        if (right_max != NULL && right_max->data > max_node->data)
            max_node = right_max;
    }
    return max_node;
}

void clone_tree(Tree *root,Tree **node)
{
    if(root==NULL)
        return;
    if(root->l!=NULL)
    {
        (*node)->l=new_node(&(*node),root->l->data);
        clone_tree(root->l,&(*node)->l);
    }
    if(root->r!=NULL)
    {
        (*node)->r=new_node(&(*node),root->r->data);
        clone_tree(root->r,&(*node)->r);
    }
}

int is_identical(Tree *r1,Tree *r2)
{
    printf("%d\n",__LINE__);
    if(r1->data != r2->data)
    {
        printf("%d\n",__LINE__);
        return 0;
    }

    if (r1 == NULL && r2 == NULL) 
    { 
        printf("%d\n",__LINE__);
        return 1;
    }

    if(!(r1->l && r2->l))
    {
        printf("%d\n",__LINE__);
        if(!(r1->l==NULL || r2->l==NULL))
        {
            printf("%d\n",__LINE__);
        return 0;
        }
    }

    if(r2->r && r2->r)
    {
        printf("%d\n",__LINE__);
        if(!(r1->r==NULL || r2->r==NULL))
        {
            printf("%d\n",__LINE__);
        return 0;
        }
    }

    if (r1->l !=NULL && r2->l!= NULL)
    {
        printf("%d\n",__LINE__);
        if(!is_identical(r1->l,r2->l))
            return 0;
    }
    if (r1->r !=NULL && r2->r!= NULL)
    {
        printf("%d\n",__LINE__);
        if(!is_identical(r1->r,r2->r))
            return 0;
    }
    printf("%d\n",__LINE__);
    return 1;
    /*
   printf("%d\n",__LINE__);
   return is_identical(r1->l,r2->l) && is_identical(r1->r,r2->r);
   */
}

int are_identical_trees(Tree *root1, Tree *root2)
{
    // If both trees are empty, they are identical
    if (root1 == NULL && root2 == NULL)
        return 1;

    // If one tree is empty and the other is not, they are not identical
    if (root1 == NULL || root2 == NULL)
        return 0;

    // If the data of the current nodes is different, trees are not identical
    if (root1->data != root2->data)
        return 0;

    // Recursively check if left and right subtrees are identical
    return (are_identical_trees(root1->l, root2->l) && are_identical_trees(root1->r, root2->r));
}

void num_of_nodes(Tree *root,int *c)
{
    if(root!=NULL)
    {
        num_of_nodes(root->l,c);
        num_of_nodes(root->r,c);
        (*c)++;
    }
}

void num_int_nodes(Tree *node,int *c)
{
    //printf("%d\n",__LINE__);
    if (node==NULL)// (!node->l && !node->r))
    {
        //printf("%d\n",__LINE__);
        return;
    }
    else if (node->l || node->r)
    {
        //printf("%d\n",__LINE__);
        (*c)++;
        //printf("%d\n",__LINE__);
        num_int_nodes(node->l,c);
        //printf("%d\n",__LINE__);
        num_int_nodes(node->r,c);
        //printf("%d\n",__LINE__);
    }
}

void num_ext_nodes(Tree *node,int *c)
{
    if (node == NULL)
        return;
    if(!node->l && !node->r)
    {
        (*c)++;
        return;
    }
    else 
    {
        num_ext_nodes(node->l,c);
        num_ext_nodes(node->r,c);
    }
}

int depth(Tree *root)
{
    if(root==NULL)
    {
        return 0;
    }
    else
    {
        int l_depth=depth(root->l);
        int r_depth=depth(root->r);
        if(l_depth>r_depth)
            return l_depth+1;
        else
            return r_depth +1;
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
                printf("Pre Order:\n");
                pre_order(root);
                printf("\n");
                break;
            }
            case 2:
            {
                printf("In Order:\n");
                in_order(root);
                printf("\n");
                break;
            }
            case 3:
            {
                printf("Post Order:\n");
                post_order(root);
                printf("\n");
                break;
            }
            case 4:
            {
                /*
                int data;
                printf("Enter the data: ");
                scanf(" %d",&data);
                */
                int n=9;
                int arr[]={39,56,78,33,54,55,80,41,25};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node(&root,arr[i]);
                }
                //add_node(&root,data);
                break;
            }
            case 5:
            {
                int data;
                printf("Enter the data to be fetched: ");
                scanf(" %d",&data);
                //printf("%d\n",__LINE__);
                Tree *node=get_node(root,data);
                printf("The fetched node's data = %d\n",node->data);
                //printf("%d\n",__LINE__);
                //printf("p=%d\tl=%d\tr=%d\n",node->p->data,node->l->data,node->r->data);
                //printf("%d\n",__LINE__);
                break;
            }
            case 6:
            {
                int data;
                printf("Enter the data to be deleted: ");
                scanf(" %d",&data);
                del_node(&root,data);
                break;
            }
            case 7:
            {
                del_tree(&root);
                free(root);
                break;
            }
            case 8:
            {
                Tree *node=smallest(root);
                printf("Smallest elem = %d\n",node->data);
                //printf("For the smallest:\np=%d\tl=%d\tr=%d\n",node->p->data,node->l-data,node->r->data);
                break;
            }
            case 9:
            {
                Tree *node=largest(root);
                printf("Largest elem = %d\n",node->data);
                //printf("For the largest:\np=%d\tl=%d\tr=%d\t",node->p->data,node->l-data,node->r->data);
                break;
            }
            case 10:
            {
                int n=9;
                int arr[]={39,56,54,78,55,80,41,25,33};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_iterative(&root,arr[i]);
                }
                break;
            }
            case 11:
            {
                //Tree **node=min_node_bt(&root);
                printf("%d\n",__LINE__);
                //printf("%d\n",(*node)->data);
                //printf("Min node of bt:\np=%d\tl=%d\tr=%d\n",node->p->data,node->l->data,node->r->data);
                break;
            }
            case 12:
            {
                //Tree *node=max_node_bt(root);
                 printf("%d\n",__LINE__);
                 //printf("%d\n",node->data);
                //("Max node of bt:\np=%d\tl=%d\tr=%d\n",node->p->data,node->l->data,node->r->data);
                break;
            }
            case 13:
            {
                if(is_bst(root))
                    printf("Binary tree is a BST\n");
                else
                    printf("Binary tree is not a bst\n");
                break;
            }
            case 14:
            {
                mirror_img(&root);
                break;
            }
            case 15:
            {
                int n=4;
                int arr[]={39,56,54,78,55,80,41,25,33};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node_bt(&root,arr[i]);
                }
                break;
            }
            case 16:
            {
                print_tree(root);
                break;
            }
            case 17:
            {
                Tree *node=find_min_node(root);
                printf("Min of bt = %d\n",node->data);
                break;
            }
            case 18:
            {
                Tree *node=find_max_node(root);
                printf("Max of bt = %d\n",node->data);
                break;
            }
            case 19:
            {
                drawTree(root);
                break;
            }
            case 20:
            {
                Tree *clone_root=new_node(&clone_root,root->data);
                clone_tree(root,&clone_root);
                printf("Pre order of clone is:\n");
                pre_order(clone_root);
                printf("\n");
                break;
            }
            case 21: //To be debugged
            {
                printf("%d\n",__LINE__);
                Tree *Root=new_node(&Root,root->data);
                
                Tree *RooT=new_node(&RooT,root->data);
                int n=9;
                int arr[]={39,56,78,33,54,55,80,41,25};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node(&RooT,arr[i]);
                }

                printf("Pre order of Root is:\n");
                pre_order(Root);
                printf("\n");

                printf("Pre order of RooT is:\n");
                pre_order(RooT);
                printf("\n");

                if(is_identical(root,Root))
                    printf("Identical\n");
                else 
                    printf("Non identical\n");

                if(is_identical(root,RooT))
                    printf("Identical\n");
                else 
                    printf("Non identical\n");
                break;
            }
            case 22:
            {
                printf("%d\n",__LINE__);
                Tree *Root=new_node(&Root,root->data);
                
                Tree *RooT=new_node(&RooT,root->data);
                int n=9;
                int arr[]={39,56,78,33,54,55,80,41,25};
                int i;
                for (i=0;i<n;i++)
                {
                    add_node(&RooT,arr[i]);
                }

                printf("Pre order of Root is:\n");
                pre_order(Root);
                printf("\n");

                printf("Pre order of RooT is:\n");
                pre_order(RooT);
                printf("\n");

                if(are_identical_trees(root,Root))
                    printf("Identical\n");
                else 
                    printf("Non identical\n");

                if(are_identical_trees(root,RooT))
                    printf("Identical\n");
                else 
                    printf("Non identical\n");
                break;
            }
            case 23:
            {
                int c=0;
                int *cnt=&c;
                num_of_nodes(root,cnt);
                printf("Total number of nodes = %d\n",*cnt);
                break;
            }
            case 24:
            {
                int c=0;
                int *cnt=&c;
                num_int_nodes(root,cnt);
                printf("%d\n",__LINE__);
                printf("The number of internal nodes = %d\n",*cnt);
                printf("%d\n",__LINE__);
                break;
            }
            case 25:
            {
                int c=0;
                int *cnt=&c;
                num_ext_nodes(root,cnt);
                printf("The number of ext nodes = %d\n",*cnt);
                break;
            }
            case 26:
            {
                printf("The depth of the tree = %d\n",depth(root));
                break;
            }
        }
    } while (ch!=0);

}
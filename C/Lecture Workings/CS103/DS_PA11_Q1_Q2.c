#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct Tree_t *Tree;

struct Tree_t
{
    int data;
    Tree left, right;
};

Tree new_node(int data)
{
    Tree tree = (Tree)calloc(1, sizeof(struct Tree_t));
    assert(tree);
    tree->data = data;
    tree->left = NULL;
    tree->right = NULL;
    return tree;
}

void in_order(Tree tree)
{
    if (!tree)
        return;
    in_order(tree->left);
    printf("%d ", tree->data);
    in_order(tree->right);
}

void pre_order(Tree tree)
{
    if (!tree)
        return;
    printf("%d ", tree->data);
    pre_order(tree->left);
    pre_order(tree->right);
}

void post_order(Tree tree)
{
    if (!tree)
        return;
    post_order(tree->left);
    post_order(tree->right);
    printf("%d ", tree->data);
}

Tree create_tree_in_post(int in[], int in_st, int in_end, int post[], int post_st, int post_end)
{
    if (in_st == in_end)
        return new_node(in[in_st]);
    if (in_st > in_end)
        return NULL;
    int i, pos;
    for (i = in_st; i <= in_end; i++)
    {
        if (post[post_end] == in[i])
        {
            pos = i;
            break;
        }
    }
    Tree left_tree = create_tree_in_post(in, in_st, pos - 1, post, post_st,  pos - 1);
    Tree right_tree = create_tree_in_post(in, pos + 1, in_end, post, pos, post_end - 1);
    Tree tree = new_node(in[pos]);
    tree->left = left_tree;
    tree->right = right_tree;
    return tree;
}

Tree create_tree_in_pre(int in[], int in_st, int in_end, int pre[], int pre_st, int pre_end)
{
    if (in_st == in_end)
        return new_node(in[in_st]);
    if (in_st > in_end)
        return NULL;
    int i, pos;
    for (i = in_st; i <= in_end; i++)
    {
        if (pre[pre_st] == in[i])
        {
            pos = i;
            break;
        }
    }
    Tree left_tree = create_tree_in_pre(in, in_st, pos - 1, pre, pre_st + 1, pre_st + pos - in_st);
    Tree right_tree = create_tree_in_pre(in, pos + 1, in_end, pre, pre_st + pos - in_st + 1, pre_st);
    Tree tree = new_node(in[pos]);
    tree->left = left_tree;
    tree->right = right_tree;
    return tree;
}

int main()
{
    int size, i;
    printf("Enter number of nodes in the tree: ");
    scanf(" %d", &size);
    printf("Enter the keys in inorder: ");
    int in[size], post[size];
    for (i = 0; i < size; i++)
    {
        scanf(" %d", &in[i]);
    }
    printf("Enter the keys in postorder: ");
    for (i = 0; i < size; i++)
    {
        scanf(" %d", &post[i]);
    }

    Tree tree = create_tree_in_post(in, 0, size - 1, post, 0, size - 1);
    printf("PreOrder: ");
    pre_order(tree);
    printf("\nInOrder: ");
    in_order(tree);
    printf("\nPostOrder: ");
    post_order(tree);

    return 0;
}

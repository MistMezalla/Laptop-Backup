#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct AVLTree_t *AVL;

struct AVLTree_t
{
    int data;
    int height;
    AVL left, right;
};

AVL new_AVL(int data)
{
    AVL avl = (AVL)calloc(1, sizeof(struct AVLTree_t));
    assert(avl);
    avl->data = data;
    avl->height = 1;
    avl->left = NULL;
    avl->right = NULL;
    return avl;
}

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int height(AVL avl)
{
    if (!avl)
        return 0;
    return avl->height;
}

int bal_factor(AVL avl)
{
    return height(avl->left) - height(avl->right);
}

AVL rotate_Right(AVL x)
{
    AVL y = x->left;
    AVL T = y->right;

    y->right = x;
    x->left = T;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

AVL rotate_Left(AVL x)
{
    AVL y = x->right;
    AVL T = y->left;

    y->left = x;
    x->right = T;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

AVL insert_AVL(AVL avl, int data)
{
    if (!avl)
        return new_AVL(data);
    if (data < avl->data)
        avl->left = insert_AVL(avl->left, data);
    else
        avl->right = insert_AVL(avl->right, data);

    avl->height = max(height(avl->left), height(avl->right)) + 1;

    int bal = bal_factor(avl);

    if (bal > 1 && data < avl->left->data) // LL case
        return rotate_Right(avl);

    if (bal < -1 && data > avl->right->data) // RR case
        return rotate_Left(avl);

    if (bal > 1 && data > avl->left->data) // LR case
    {
        avl->left = rotate_Left(avl->left);
        return rotate_Right(avl);
    }

    if (bal < -1 && data < avl->right->data) // RL case
    {
        avl->right = rotate_Right(avl->right);
        return rotate_Left(avl);
    }

    return avl;
}

AVL delete_AVL(AVL avl, int data)
{
    if (!avl)
        return NULL;

    if (data < avl->data)
        avl->left = delete_AVL(avl->left, data);
    else if (data > avl->data)
        avl->right = delete_AVL(avl->right, data);
    else
    {
        if (!avl->left || !avl->right)
        {
            AVL temp = avl->left ? avl->left : avl->right;
            if (!temp)
            {
                temp = avl;
                avl = NULL;
            }
            else
                *avl = *temp;
            free(temp);
        }
        else
        {
            AVL successor = avl->right;
            while (successor->left)
                successor = successor->left;

            avl->data = successor->data;
            avl->right = delete_AVL(avl->right, successor->data);
        }
    }

    if (!avl)
        return NULL;

    avl->height = max(height(avl->left), height(avl->right)) + 1;

    int bal = bal_factor(avl);

    if (bal > 1 && bal_factor(avl->left) >= 0) // LL case
        return rotate_Right(avl);

    if (bal > 1 && bal_factor(avl->left) < 0) // LR case
    {
        avl->left = rotate_Left(avl->left);
        return rotate_Right(avl);
    }

    if (bal < -1 && bal_factor(avl->right) <= 0) // RR case
        return rotate_Left(avl);

    if (bal < -1 && bal_factor(avl->right) > 0) // RL case
    {
        avl->right = rotate_Right(avl->right);
        return rotate_Left(avl);
    }

    return avl;
}

void print_AVL(AVL avl) {
    if (avl) {
        print_AVL(avl->left);
        printf("%d ", avl->data);
        print_AVL(avl->right);
    }
}

void print_tree_structure(AVL avl, int level) {
    if (avl) {
        print_tree_structure(avl->right, level + 1);
        for (int i = 0; i < level; i++)
            printf("    ");
        printf("%d\n", avl->data);
        print_tree_structure(avl->left, level + 1);
    }
}

void main()
{
    AVL avl = NULL;
    avl = insert_AVL(avl, 5);
    avl = insert_AVL(avl, 7);
    avl = insert_AVL(avl, 1);
    avl = insert_AVL(avl, 9);
    print_AVL(avl);
    printf("\n");

    print_tree_structure(avl,0);
    printf("\n");

    avl = delete_AVL(avl, 1);
    print_AVL(avl);
    printf("\n");

    print_tree_structure(avl,0);
    printf("\n");
}

// Iterative Queue based C program
// to do level order traversal
// of Binary Tree
#include <stdio.h>
#include <stdlib.h>
#define MAX_Q_SIZE 500
 
// A binary tree node has data,
// pointer to left child
// and a pointer to right child
struct node {
    int data;
    struct node* left;
    struct node* right;
};
 
// Function prototypes
struct node** createQueue(int*, int*);
void enQueue(struct node**, int*, struct node*);
struct node* deQueue(struct node**, int*);
 
// Given a binary tree, print its nodes in level order
// using array for implementing queue
void printLevelOrder(struct node* root)
{
    int rear, front;
    struct node** queue = createQueue(&front, &rear);
    struct node* temp_node = root;
 
    while (temp_node) {
        printf("%d ", temp_node->data);
 
        // Enqueue left child
        if (temp_node->left)
            enQueue(queue, &rear, temp_node->left);
 
        // Enqueue right child
        if (temp_node->right)
            enQueue(queue, &rear, temp_node->right);
 
        // Dequeue node and make it temp_node
        temp_node = deQueue(queue, &front);
    }
}

// Function to check if the queue is empty
int isEmpty(struct node** queue)
{
    // If the queue is NULL or the front and rear pointers coincide, the queue is empty
    return (queue == NULL || queue[0] == NULL);
}

// Given a binary tree, print its nodes in level order
// using array for implementing queue
void print_lvl_order(struct node* root)
{
    if (root == NULL)
        return;

    int rear, front;
    struct node** queue = createQueue(&front, &rear);
    struct node* temp_node = root;

    // Enqueue root and a NULL marker to indicate the end of the level
    enQueue(queue, &rear, temp_node);
    enQueue(queue,&rear, NULL);

    // Loop until the queue is empty
    while (!isEmpty(queue)) {
        // Dequeue a node
        temp_node = deQueue(queue,&front);

        // If the dequeued node is NULL, it means the level has ended
        // Print a newline and enqueue the next level's NULL marker if there are remaining nodes
        if (temp_node == NULL) {
            printf("\n");
            if (!isEmpty(queue))
                enQueue(queue, &rear, NULL);
        } else {
            // Print the data of the dequeued node
            printf("%d ", temp_node->data);

            // Enqueue the left and right children if they exist
            if (temp_node->left)
                enQueue(queue,  &rear, temp_node->left);
            if (temp_node->right)
                enQueue(queue,  &rear, temp_node->right);
        }
    }

    // Free the dynamically allocated memory for the queue
    free(queue);
}

// Utility functions
struct node** createQueue(int* front, int* rear)
{
    struct node** queue = (struct node**)malloc(
        sizeof(struct node*) * MAX_Q_SIZE);
 
    *front = *rear = 0;
    return queue;
}
 
void enQueue(struct node** queue, int* rear,
             struct node* new_node)
{
    queue[*rear] = new_node;
    (*rear)++;
}
 
struct node* deQueue(struct node** queue, int* front)
{
    (*front)++;
    return queue[*front - 1];
}
 
// Helper function that allocates a new node with the
// given data and NULL left and right pointers.
struct node* newNode(int data)
{
    struct node* node
        = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
 
    return (node);
}
 
// Driver program to test above functions
int main()
{
    struct node* root = newNode(4);
    root->left = newNode(2);
    root->right = newNode(6);
    root->left->left = newNode(1);
    root->left->right = newNode(3);
    root->right->left = newNode(5);
    root->right->right = newNode(7);
 
    printf("Level Order traversal of binary tree is \n");
    printLevelOrder(root);
    printf("\n");
    print_lvl_order(root);
 
    return 0;
}


#include <stdio.h>
#include <stdlib.h>

typedef struct que
{
    int *arr;
    int front;
    int rear;
    int size;
} CircularQueue;

CircularQueue *new_circular_queue(int max_size) 
{
    CircularQueue *queue = (CircularQueue *)malloc(sizeof(CircularQueue));
    queue->arr = (int *)malloc(max_size * sizeof(int));
    queue->front = -1;
    queue->rear = -1;
    queue->size = max_size;
    return queue;
}

int is_empty(CircularQueue *queue) 
{
    return (queue->front == -1);
}

int is_full(CircularQueue *queue) 
{
    return ((queue->rear + 1) % queue->size == queue->front);
}

void enqueue(CircularQueue *queue, int value) 
{
    if (is_full(queue)) 
    {
        printf("Queue is full\n");
        return;
    }
    if (is_empty(queue))
        queue->front = 0;
    queue->rear = (queue->rear + 1) % queue->size;
    queue->arr[queue->rear] = value;
}

int dequeue(CircularQueue *queue) 
{
    if (is_empty(queue)) 
    {
        printf("Queue is empty\n");
        return -1;
    }
    int val = queue->arr[queue->front];
    if (queue->front == queue->rear) 
    {
        queue->front = -1;
        queue->rear = -1;
    } 
    else 
    {
        queue->front = (queue->front + 1) % queue->size;
    }
    return val;
}

int front(CircularQueue *queue) 
{
    if (is_empty(queue)) 
    {
        printf("Queue is empty\n");
        return -1;
    }
    return queue->arr[queue->front];
}

int rear(CircularQueue *queue) 
{
    if (is_empty(queue)) 
    {
        printf("Queue is empty\n");
        return -1;
    }
    return queue->arr[queue->rear];
}

void main() 
{
    int max_size;
    printf("Enter the maximum size of the queue: ");
    scanf("%d", &max_size);

    CircularQueue *queue = new_circular_queue(max_size);

    int ch;
    do {
        printf("Enter the choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                if (is_empty(queue))
                    printf("Queue is empty\n");
                else
                    printf("Queue is not empty\n");
                break;
            case 2:
                if (is_full(queue))
                    printf("Queue is full\n");
                else
                    printf("Queue is not full\n");
                break;
            case 3:
                printf("Enter the value to enqueue: ");
                int value;
                scanf("%d", &value);
                enqueue(queue, value);
                break;
            case 4:
                printf("Dequeued item: %d\n", dequeue(queue));
                break;
            case 5:
                printf("Item at the front: %d\n", front(queue));
                break;
            case 6:
                printf("Item at the rear: %d\n", rear(queue));
                break;
        }
    } while (ch != 0);
    free(queue->arr);
    free(queue);
}

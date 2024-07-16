#include <stdio.h>
#include <stdlib.h>

#define PARENT(i) ((i - 1) / 2)
#define LEFT(i) (2 * i + 1)
#define RIGHT(i) (2 * i + 2)

typedef struct 
{
    int* array;
    int capacity;
    int size;
} priority_queue;

priority_queue* create_priority_queue(int capacity) 
{
    priority_queue* pq = (priority_queue*)malloc(sizeof(priority_queue));
    pq->capacity = capacity;
    pq->size = 0;
    pq->array = (int*)malloc(capacity * sizeof(int));
    return pq;
}

void max_heapify(int arr[], int n, int i) 
{
    int largest = i;
    int left = LEFT(i);
    int right = RIGHT(i);

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) 
    {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        max_heapify(arr, n, largest);
    }
}

void enqueue(priority_queue* pq, int item) 
{
    if (pq->size == pq->capacity) 
    {
        printf("Queue is full. Cannot enqueue.\n");
        return;
    }

    int i = pq->size;
    pq->size++;
    pq->array[i] = item;

    while (i != 0 && pq->array[PARENT(i)] < pq->array[i]) 
    {
        int temp = pq->array[i];
        pq->array[i] = pq->array[PARENT(i)];
        pq->array[PARENT(i)] = temp;
        i = PARENT(i);
    }
}

int dequeue(priority_queue* pq) 
{
    if (pq->size == 0) 
    {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1;
    }

    int item = pq->array[0];
    pq->array[0] = pq->array[pq->size - 1];
    pq->size--;
    max_heapify(pq->array, pq->size, 0);

    return item;
}

void print_priority_queue(priority_queue* pq) 
{
    if (pq->size == 0) {
        printf("Priority Queue is empty.\n");
        return;
    }

    printf("Priority Queue: ");
    for (int i = 0; i < pq->size; i++) 
    {
        printf("%d ", pq->array[i]);
    }
    printf("\n");
}

void main() 
{
    priority_queue* pq = create_priority_queue(10);

    enqueue(pq, 10);
    enqueue(pq, 20);
    enqueue(pq, 15);
    enqueue(pq, 5);

    print_priority_queue(pq);

    printf("Dequeued item: %d\n", dequeue(pq));
    printf("Dequeued item: %d\n", dequeue(pq));

    print_priority_queue(pq);
}

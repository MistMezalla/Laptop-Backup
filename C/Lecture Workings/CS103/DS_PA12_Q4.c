#include <stdio.h>

#define LEFT(i) (2 * (i) + 1)
#define RIGHT(i) (2 * (i) + 2)

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

void build_max_heap(int arr[], int n) 
{
    for (int i = n / 2 - 1; i >= 0; i--) 
    {
        max_heapify(arr, n, i);
    }
}

void heap_sort(int arr[], int n) 
{
    build_max_heap(arr, n);
    for (int i = n - 1; i > 0; i--) 
    {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        max_heapify(arr, i, 0);
    }
}

void print_array(int arr[], int n) 
{
    for (int i = 0; i < n; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: \n");
    print_array(arr, n);

    heap_sort(arr, n);

    printf("Sorted array: \n");
    print_array(arr, n);
}

#include <bits/stdc++.h>
using namespace std;

class Max_Priority_Queues {
private:
    vector<int> arr;
    int heap_size;

    void Max_Heapify(int i) {
        int largest = i;
        int left = 2 * i;
        int right = 2 * i + 1;

        if (left <= heap_size && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right <= heap_size && arr[right] > arr[largest]) {
            largest = right;
        }
        if (largest != i) {
            swap(arr[i], arr[largest]);
            Max_Heapify(largest);
        }
    }

public:
    Max_Priority_Queues(int size = 0) : heap_size(size) {
        arr.push_back(numeric_limits<int>::infinity()); 
    }

    void Build_max_heap(vector<int>& input) {
        for (int i = 0; i < input.size(); i++) {
            arr.push_back(input[i]);
            heap_size++;
        }

        for (int i = heap_size / 2; i > 0; i--) {
            Max_Heapify(i);
        }
    }

    void Asc_heap_sort() {
        while (heap_size > 1) {
            del_max();
        }
    }

    void print_arr() {
        for (int i = 1; i <= heap_size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void insert_max_heap(int num) {
        arr.push_back(num);
        heap_size++;
        int i = heap_size;

        while (i > 1 && arr[i / 2] < arr[i]) {
            swap(arr[i], arr[i / 2]);
            i = i / 2;
        }
    }

    int del_max() {
        int max_elem = arr[1];
        arr[1] = arr[heap_size];
        heap_size--;
        Max_Heapify(1);
        return max_elem;
    }
};

int main() {
    Max_Priority_Queues max_heap;
    vector<int> input = {8, 7, 12, 20, 25, 7, 18};
    max_heap.Build_max_heap(input);
    max_heap.print_arr();

    max_heap.insert_max_heap(35);
    max_heap.print_arr();

    cout << max_heap.del_max() << endl;
    max_heap.print_arr();

    max_heap.Asc_heap_sort();
    max_heap.print_arr();

    return 0;
}

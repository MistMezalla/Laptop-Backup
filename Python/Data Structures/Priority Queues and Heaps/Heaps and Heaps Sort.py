N = 20
# 1 indexed based implementation
class Max_Priority_Queues:
    def __init__(self,size = 0):
        self.arr = ['inf']
        self.heap_size = size

    def Max_Heapify(self,i):
        nums = self.arr

        largest = i
        if 2*i <= self.heap_size and nums[i] < nums[2*i]:
            largest = 2 * i
        if 2*i+1 <= self.heap_size and nums[largest] < nums[2*i+1]:
            largest = 2 *i +1

        if largest != i:
            nums[i],nums[largest] = nums[largest],nums[i]
            self.Max_Heapify(largest)

    def Build_max_heap(self,arr):
        for i in range(len(arr)):
            self.arr.append(arr[i])
            self.heap_size += 1

        for i in range(self.heap_size//2,0,-1):
            self.Max_Heapify(i)

    def Asc_heap_sort(self):
        for _ in range(self.heap_size):
            self.del_max()

        return self.arr[1:]

    def print_arr(self):
        for i in range(1,len(self.arr)):
            print(self.arr[i],end = " ")

    def insert_max_heap(self,num):
        self.arr.append(num)
        self.heap_size += 1
        i = self.heap_size

        while i > 1 and self.arr[i // 2] < self.arr[i]:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i = i // 2

    def del_max(self):
        max_elem = self.arr[1]
        self.arr[1],self.arr[self.heap_size] = self.arr[self.heap_size],self.arr[1]
        self.heap_size -= 1
        self.Max_Heapify(1)
        return max_elem

max_heap = Max_Priority_Queues()
max_heap.Build_max_heap([8,7,12,20,25,7,18])
max_heap.print_arr()
print()
max_heap.insert_max_heap(35)
max_heap.print_arr()
print()
print(max_heap.del_max())
max_heap.print_arr()
print()
print(max_heap.Asc_heap_sort())
max_heap.print_arr()
print()

class Min_Priority_Queues():
    def __init__(self,size=0):
        self.arr = ['inf']
        self.heap_size = size

    def Min_Heapify(self,i):
        smallest = i

        if 2 * i <= self.heap_size and self.arr[i] > self.arr[2*i]:
            smallest = 2 * i
        if 2 * i +1 <= self.heap_size and self.arr[smallest] > self.arr[2*i+1]:
            smallest = 2*i+1

        if smallest != i:
            self.arr[i],self.arr[smallest] = self.arr[smallest],self.arr[i]
            self.Min_Heapify(smallest)

    def Build_min_heap(self,arr):
        for i in range(len(arr)):
            self.arr.append(arr[i])
            self.heap_size = i+1

        for i in range(self.heap_size//2,0,-1):
            self.Min_Heapify(i)

    def insert_min(self,num):
        self.arr.append(num)
        self.heap_size += 1
        i = self.heap_size

        while i > 1 and self.arr[i // 2] > self.arr[i]:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i = i // 2

    def del_min(self):
        min_elem = self.arr[1]

        self.arr[1],self.arr[self.heap_size] = self.arr[self.heap_size],self.arr[1]
        self.heap_size -= 1
        self.Min_Heapify(1)

        return min_elem

    def Desc_heap_sort(self):
        for i in range(self.heap_size):
            self.del_min()

        return self.arr[1:]

    def print_arr(self):
        for i in range(1, len(self.arr)):
            print(self.arr[i], end=" ")




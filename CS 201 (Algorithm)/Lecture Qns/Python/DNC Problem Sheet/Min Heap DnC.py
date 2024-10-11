class Solution:

    def heapify(self, arr, n, i):
        """
        Heapify the subtree rooted at index i. Assumes that the left and right
        subtrees are already heapified. This is a bottom-up heapify process.
        """
        smallest = i  # Initialize smallest as the root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # If left child exists and is smaller than the root
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # If right child exists and is smaller than the current smallest
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # If the smallest is not the root, swap and continue heapifying
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def build_min_heap(self, arr):
        """
        Build a min heap from an array in-place using the bottom-up heapify approach.
        """
        n = len(arr)
        # Start from the last internal node and heapify each node up to the root
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def construct_min_heap(self, arr):
        """
        Top-level function to construct the min heap.
        """
        self.build_min_heap(arr)

    def print_heap(self, arr):
        """
        Prints the min-heap array in a readable format (level-wise).
        """
        n = len(arr)
        level = 0
        i = 0
        while i < n:
            level_size = 2 ** level
            print('Level', level, ':', arr[i:i + level_size])
            i += level_size
            level += 1


# Example usage
sol = Solution()
arr = [3, 1, 6, 5, 2, 8, 7]
sol.construct_min_heap(arr)

# Output the heap structure
print("Min Heap Array Representation:")
sol.print_heap(arr)

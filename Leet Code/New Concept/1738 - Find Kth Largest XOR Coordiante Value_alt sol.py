'''
-> My Intuition:- (Correct)
    -> Sort and return kth smallest
    -> However tried to think for DnC approach which I cldn't find.

-> Below Intuition:-
    -> Approach 1:-
        -> Sort
        -> return kth smallest

    -> Approach 2:-
        -> Use 'min heap'
        -> Push into heap
        -> pop from heap if len(heap) > k
        -> return top most elem:
            -> as heaps size is k
            -> heap is a min heap
            -> and asked for kth 'largest' elem
'''
class Solution1:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i:
                    matrix[i][j] ^= matrix[i-1][j]
                if j:
                    matrix[i][j] ^= matrix[i][j-1]
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j-1]
                res.append(matrix[i][j])

        res.sort(reverse=True)
        return res[k-1]

sol = Solution1()
print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 1))
print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 2))
print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 3))
print(sol.kthLargestValue(matrix = [[5,2],[1,6]], k = 4))

import heapq
class Solution2:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        min_heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i:
                    matrix[i][j] ^= matrix[i-1][j]
                if j:
                    matrix[i][j] ^= matrix[i][j-1]
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j-1]

                heapq.heappush(min_heap,matrix[i][j])
                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return min_heap[0]

sol2 = Solution2()
print(sol2.kthLargestValue(matrix = [[5,2],[1,6]], k = 1))
print(sol2.kthLargestValue(matrix = [[5,2],[1,6]], k = 2))
print(sol2.kthLargestValue(matrix = [[5,2],[1,6]], k = 3))
print(sol2.kthLargestValue(matrix = [[5,2],[1,6]], k = 4))






import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)

        op = 0
        while min_heap[0] < k:
            elem1, elem2 = heapq.heappop(min_heap),heapq.heappop(min_heap)
            heapq.heappush(min_heap,2*elem1+elem2)

            op += 1

        return op

sol =  Solution()
print(sol.minOperations(nums = [2,11,10,1,3], k = 10))
print(sol.minOperations(nums = [1,1,2,4,9], k = 20))
print(sol.minOperations([1,2,3,10,25,26,27],20))


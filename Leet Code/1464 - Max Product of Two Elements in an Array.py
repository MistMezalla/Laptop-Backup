import heapq
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        return ( -heapq.heappop(max_heap) - 1) * ( -heapq.heappop(max_heap) - 1)

sol = Solution()
print(sol.maxProduct([3,4,5,2]))
print(sol.maxProduct([7,16]))



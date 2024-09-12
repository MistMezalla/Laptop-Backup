import heapq
from math import ceil
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        max_heap = [-x for x in piles]

        heapq.heapify(max_heap)

        for i in range(k):
            heapq.heappush(max_heap,-ceil(-heapq.heappop(max_heap)/2))

        return -sum(max_heap)

sol = Solution()
print(sol.minStoneSum(piles = [5,4,9], k = 2))
print(sol.minStoneSum([10],1))



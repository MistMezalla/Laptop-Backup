import heapq
from math import isqrt
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        max_heap = [-x for x in gifts]

        heapq.heapify(max_heap)

        for i in range(k):
            heapq.heappush(max_heap,-isqrt(-heapq.heappop(max_heap)))

        return -sum(max_heap)

sol =  Solution()
print(sol.pickGifts(gifts = [25,64,9,4,100], k = 4))
print(sol.pickGifts(gifts = [1,1,1,1], k = 4))



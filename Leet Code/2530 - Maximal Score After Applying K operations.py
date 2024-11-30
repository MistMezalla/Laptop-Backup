import heapq
from math import ceil
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        while k:
            elem = -heapq.heappop(max_heap)
            heapq.heappush(max_heap,-ceil(elem/3))
            score += elem
            k-=1

        return score



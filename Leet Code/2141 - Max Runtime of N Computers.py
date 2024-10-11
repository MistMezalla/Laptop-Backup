import heapq
from math import log2,ceil
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        max_heap = [-x for x in batteries]
        heapq.heapify(max_heap)

        time = 0
        while len(max_heap) >= n:
            time_used = float('inf')
            used_batteries = []
            for _ in  range(n):
                elem = -heapq.heappop(max_heap)
                time_used = min(time_used,elem - ceil(log2(elem)))
                used_batteries.append(elem)

            for life in used_batteries:
                if life - time_used:
                    heapq.heappush(max_heap,-(life-time_used))
            time += time_used

        return time

sol = Solution()
print(sol.maxRunTime( n = 2, batteries = [3,3,3]))


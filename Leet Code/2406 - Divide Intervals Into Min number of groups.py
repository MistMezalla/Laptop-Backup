import heapq
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        min_heap = []

        for st,end in intervals:
            if min_heap and st > min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap,end)


        return len(min_heap)
import heapq

class Solution:
    def min_classrooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])

        return len(heap)

sol = Solution()
print(sol.min_classrooms([(30, 75), (0, 50), (60, 150)]))

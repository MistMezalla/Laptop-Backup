import heapq
class Solution:
    def fillCups(self, amount: list[int]) -> int:
        max_heap = [-x for x in amount if x]

        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            if len(max_heap)>=2:
                cup1,cup2 = -heapq.heappop(max_heap)-1,-heapq.heappop(max_heap)-1
            else:
                cup1 = -heapq.heappop(max_heap)-1
                cup2 = 0
            time += 1

            if cup1:
                heapq.heappush(max_heap,-cup1)
            if cup2:
                heapq.heappush(max_heap,-cup2)

        return time

sol = Solution()
print(sol.fillCups([1,4,2]))
print(sol.fillCups([5,4,4]))
print(sol.fillCups([5,0,0]))





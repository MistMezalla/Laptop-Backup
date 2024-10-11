import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_heap = []

        heapq.heappush(max_heap,-a)
        heapq.heappush(max_heap, -b)
        heapq.heappush(max_heap, -c)

        cnt = 0
        while len(max_heap) > 1:
            elem1,elem2 = -heapq.heappop(max_heap) - 1,-heapq.heappop(max_heap) - 1
            cnt += 1

            if elem1:
                heapq.heappush(max_heap,-elem1)
            if elem2:
                heapq.heappush(max_heap,-elem2)

        return cnt

sol = Solution()
print(sol.maximumScore(8,8,1))
print(sol.maximumScore(4,2,4))



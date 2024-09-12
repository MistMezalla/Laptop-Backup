import heapq
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        min_heap = nums
        heapq.heapify(min_heap)

        res = []
        while min_heap:
            Alice = heapq.heappop(min_heap)
            Bob = heapq.heappop(min_heap)

            res.append(Bob)
            res.append(Alice)

        return res

sol = Solution()
print(sol.numberGame([5,4,2,3]))
print(sol.numberGame([2,4]))
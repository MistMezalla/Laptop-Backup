import heapq
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        min_heap = [x for x in nums if x]
        if not min_heap:
            return 0

        heapq.heapify(min_heap)

        cnt = 1
        prev_elem = heapq.heappop(min_heap)
        while min_heap:
            curr_elem = heapq.heappop(min_heap)
            cnt += 1 if curr_elem != prev_elem else 0
            prev_elem = curr_elem

        return cnt

sol = Solution()
print(sol.minimumOperations([1,0,5,3,5]))
print(sol.minimumOperations([0]))
print(sol.minimumOperations([2,2,4,8]))

class Solution_alt:
    def minimumOperations(self, nums: list[int]) -> int:
        min_heap = [x for x in nums if x]

        return len(set(min_heap))

sol_alt = Solution_alt()
print(sol_alt.minimumOperations([1,0,5,3,5]))
print(sol_alt.minimumOperations([0]))
print(sol_alt.minimumOperations([2,2,4,8]))




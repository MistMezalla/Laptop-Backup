import heapq
class Solution:
    def findScore(self, nums: list[int]) -> int:
        marked = [0]*len(nums)

        min_heap = [(val,ind) for ind,val in enumerate(nums)]
        heapq.heapify(min_heap)

        res = 0
        while min_heap:
            val,ind = heapq.heappop(min_heap)

            if marked[ind]:
                continue

            res += val
            marked[ind] = 1
            if ind + 1 < len(nums):
                marked[ind+1] = 1
            if ind - 1 >= 0:
                marked[ind-1] = 1

        return res

sol = Solution()
print(sol.findScore(nums = [2,1,3,4,5,6]))
print(sol.findScore(nums = [2,3,5,1,3,2]))

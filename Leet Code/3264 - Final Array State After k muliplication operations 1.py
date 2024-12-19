import heapq
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        #hash_ind = {ind: val for ind,val in enumerate(nums)}

        min_heap = [(val,ind) for ind,val in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            temp,ind = heapq.heappop(min_heap)
            nums[ind] *= multiplier
            heapq.heappush(min_heap,(nums[ind],ind))

        # for val,ind in min_heap:
        #     nums[ind] = val

        return nums

sol = Solution()
print(sol.getFinalState([2,4,4,2,8],5,2))







import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        return nums.index(k)
        
sol = Solution()
print(sol.minOperations(nums = [2,11,10,1,3], k = 10))
print(sol.minOperations(nums = [1,1,2,4,9], k = 1))
print(sol.minOperations(nums = [1,1,2,4,9], k = 9))
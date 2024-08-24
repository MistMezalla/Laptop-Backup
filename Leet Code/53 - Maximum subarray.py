'''
-> This solution's algo is taken from class
-> This algo is also called "Kadane's Algo"
-> Try to solve using dp concepts upon completing dp
'''
'''
Resolve = 1
Revise = 2
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_suff = nums[0]
        max_subarr = nums[0]

        for i in range(1,len(nums)):
            max_suff = max(nums[i],nums[i] + max_suff)
            max_subarr = max(max_suff,max_subarr)

        return max_subarr

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5,4,-1,7,8]))
print(sol.maxSubArray([-5,-4,-1,-7,-8]))



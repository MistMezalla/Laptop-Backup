class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        res = [nums[0]]
        total = [nums[0]]

        curr_sum = nums[0]
        n = 2*len(nums) - 1
        for i in range(1,n):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i % len(nums)]
            total.append(curr_sum)
            res.append(max(res[-1],total[-1]))

        MSA = res[0+len(nums) - 1]

        for i in range(1,len(nums)):
            curr_MSA = res[i+len(nums) - 1] - total[i-1] if res[i+len(nums) - 1] >= 0 and total[i-1] >= 0 else res[i+len(nums) - 1]
            MSA = max(MSA,curr_MSA)

        return MSA

sol = Solution()
print(sol.maxSubarraySumCircular([5,-3,5,1]))
print(sol.maxSubarraySumCircular([5,1,-3,5]))
print(sol.maxSubarraySumCircular([-3,-2,-3]))
print(sol.maxSubarraySumCircular([-3,5,1,-6,7]))



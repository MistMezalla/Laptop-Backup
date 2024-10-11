from math import ceil
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = ceil(sum(nums)/2)
        if n * 2 != sum(nums):
            return False

        dp = [[-1]*len(nums) for _ in range(n+1)]

        for i in range(n+1):
            if i >= nums[-1]:
                dp[i][-1] = nums[-1]
            else:
                dp[i][-1] = 0

        for j in range(len(nums)-2,-1,-1):
            for i in range(n+1):
                res1 = 0
                res2 = dp[i][j+1]
                if i >= nums[j]:
                    res1 = dp[i - nums[j]][j+1] + nums[j]

                dp[i][j] = max(res1,res2)

        if dp[n][0] == n:
            return True
        return False

sol = Solution()
print(sol.canPartition([5,1,11,5]))
print(sol.canPartition([1,2,3,4]))
print(sol.canPartition([1,2,3,5]))
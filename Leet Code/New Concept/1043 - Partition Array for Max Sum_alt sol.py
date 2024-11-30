'''
-> See the supplementary material for the understanding the logic of below code.
'''
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for start in range(len(arr)-1,-1,-1):
            curr_Max = 0
            end = min(len(arr),start+k)

            for i in range(start,end):
                curr_Max = max(curr_Max,arr[i])
                dp[start] = max(dp[start],dp[i+1] + curr_Max*(i - start + 1))

        return dp[0]

sol = Solution()
print(sol.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,8,9,3],4))
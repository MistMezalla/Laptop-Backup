class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0

        for i in range(len(nums)-1):
            moves += (nums[i+1] - nums[i])*(len(nums) - 1 - i)

        return moves

        #return sum(nums) - min(nums) * len(nums)

sol = Solution()
print(sol.minMoves([3,1,8,14,15]))
print(sol.minMoves([3,1,2]))
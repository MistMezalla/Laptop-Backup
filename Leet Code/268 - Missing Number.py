class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        Sum = sum(i for i in range(len(nums) + 1))
        sum_nums = sum(nums[i] for i in range(len(nums)))

        return Sum - sum_nums

sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))


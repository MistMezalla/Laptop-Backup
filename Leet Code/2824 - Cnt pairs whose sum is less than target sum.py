class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1

        cnt = 0
        while left <= right:
            if nums[left] + nums[right] < target:
                cnt += right - left
                left += 1
            else:
                right -= 1

        return cnt

sol = Solution()
print(sol.countPairs([-1,1,2,3,1],3))


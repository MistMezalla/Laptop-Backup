class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_pro = float('-inf')

        curr_pro = 1
        for num in nums:
            curr_pro *= num
            max_pro = max(max_pro,curr_pro)

            if curr_pro == 0:
                curr_pro = 1

        curr_pro = 1
        for i in range(len(nums) - 1,-1,-1):
            curr_pro *= nums[i]
            max_pro = max(max_pro,curr_pro)

            if curr_pro == 0:
                curr_pro = 1

        return max_pro

sol = Solution()
print(sol.maxProduct([2,3,-1,6,8,0,-2,10,4,-1]))


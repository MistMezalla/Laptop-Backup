class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:

        l1 = 1
        max_len = 1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l1+=1
            else:
                max_len = max(max_len,l1)
                l1 = 1


        return max(max_len,l1)

sol = Solution()
print(sol.findLengthOfLCIS([1,2,3,6,4,8,7,10,11]))
print(sol.findLengthOfLCIS([1,3,5,7]))

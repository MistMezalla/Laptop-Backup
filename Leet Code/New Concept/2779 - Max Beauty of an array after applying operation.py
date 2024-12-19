'''
-> Well the intuition that the sol will be based in bin search was right but cldn't find a concrete sol method that
wld have served as the algo
'''

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()

        max_len = 0
        for ind,num in enumerate(nums):
            curr_len = self.upper_bound(nums,num + 2*k) - ind + 1
            max_len = max(max_len,curr_len)

        return max_len


    def upper_bound(self,nums,val):
        lo,hi = 0,len(nums)-1
        res = 0

        while hi - lo > -1:
            mid = (hi + lo)//2

            if nums[mid] <= val:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res

sol = Solution()
print(sol.maximumBeauty([4,6,1,2],2))

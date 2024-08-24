class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return self._findPeakElem(nums,0,len(nums)-1)

    def _findPeakElem(self,nums,lo,hi):
        if hi == lo:
            return lo

        mid = (hi+lo)//2

        if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == hi or nums[mid] > nums[mid+1]):
            return mid

        elif mid>0 and nums[mid] < nums[mid-1]:
            return self._findPeakElem(nums,lo,mid-1)

        else:
            return self._findPeakElem(nums,mid+1,hi)

sol = Solution()
print(sol.findPeakElement([2,8]))

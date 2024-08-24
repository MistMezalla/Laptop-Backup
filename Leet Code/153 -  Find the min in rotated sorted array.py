class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        min_elem = float('inf')
        while hi - lo > -1:
            mid = (hi + lo)//2

            if nums[lo] <= nums[mid]:
                min_elem = min(nums[lo],min_elem)
                lo = mid + 1
            else:
                min_elem = min(nums[mid],min_elem)
                hi = mid - 1

        return min_elem

sol = Solution()
print(sol.findMin([2,4,5,6,7,0,1,]))


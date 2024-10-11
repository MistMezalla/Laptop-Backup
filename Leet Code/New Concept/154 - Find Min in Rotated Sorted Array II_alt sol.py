class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0,len(nums) - 1

        while hi - lo > 0:
            mid = (hi +lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[lo] > nums[mid]:
                hi = mid
            else:
                hi -= 1

        return nums[lo]

sol = Solution()
print(sol.findMin([3,1]))
print(sol.findMin([1,2,3,0]))
print(sol.findMin([3,4,5,6,1,2]))
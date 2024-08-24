class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo,hi = 0,len(nums)-1

        while hi - lo > -1 :
            mid = (hi + lo) // 2

            if nums[mid] > nums[hi]: # => min in RHS
                lo = mid + 1
            elif nums[lo] > nums[mid]: # => min in LHS
                hi = mid
            else:
                hi -= 1

        return nums[lo]

sol = Solution()
print(sol.findMin([3,1]))
print(sol.findMin([1,1,1]))
print(sol.findMin([2,2,2,2,2,4,4,4,4,4,0,1,1,1,1,1,2,2,2]))
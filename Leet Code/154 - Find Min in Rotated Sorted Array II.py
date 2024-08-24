class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        min_elem = float('inf')
        while hi - lo > -1:
            mid = (hi + lo)//2

            if nums[mid] < min_elem:
                min_elem = min(min_elem,nums[mid])

            if nums[lo] == nums[mid]:
                lo += 1
                continue

            if nums[lo] < nums[mid]:
                min_elem = min(min_elem,nums[lo])
                lo = mid + 1

            else:
                min_elem = min(min_elem,nums[mid])
                hi = mid - 1

        return min_elem #if min_elem != float('inf') else nums[0]

sol = Solution()
print(sol.findMin([3,1]))
print(sol.findMin([1,1,1]))
print(sol.findMin([2,2,2,2,2,4,4,4,4,4,0,1,1,1,1,1,2,2,2]))


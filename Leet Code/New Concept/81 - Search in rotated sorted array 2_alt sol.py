'''
-> Same intuition as Q33
'''


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0,len(nums) - 1

        while hi - lo > 1:
            mid = (hi+lo)//2

            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        if nums[hi] == target or nums[lo] == target:
            return True
        else:
            return False

sol = Solution()
print(sol.search([1,0,1,1,1],0))

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo,hi = 0,len(nums) - 1

        while hi - lo > 1:
            mid = (hi + lo)//2

            if nums[mid] == target:
                return True

            if nums[lo] == nums[mid]: #to handle case where lo,hi and mid are duplicates and finding sorted subarr
                lo+=1                 # becomes a challenge without this condition
                continue

            elif nums[mid] > nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        if nums[lo] == target or nums[hi] == target:
            return True
        else:
            return False


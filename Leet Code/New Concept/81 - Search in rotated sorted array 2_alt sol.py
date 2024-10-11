'''
-> Same intuition as Q33
'''


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1

        while hi - lo > 0:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid]:
                lo += 1
                continue
            if nums[mid] > nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= nums[hi]:  # nums[mid] < nums[hi] -> Error as abv  only [lo] == [mid] handled. So [mid]
                                        # <= [hi] is neccessary here.
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return True if nums[lo] == target else False
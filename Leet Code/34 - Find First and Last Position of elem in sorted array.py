'''
-> Improvement: Cld have made a function for binary search to avoid repeated lines of code
'''

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = 0
        hi = len(nums) - 1
        ans = [-1,-1]

        ind = None
        while lo <= hi:
            mid = (hi + lo)//2

            if nums[mid] == target:
                ind = mid
                break

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        if ind == None:
            return ans

        lo = 0
        hi = ind
        while hi - lo > 1:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                hi = mid - 1
            else:
                lo = mid

        if nums[hi] != target:
            ans[0] = (hi+1)
        elif nums[lo] != target:
            ans[0] = (lo+1)
        else:
            ans[0] = (lo)

        lo = ind
        hi = len(nums) - 1

        while hi - lo > 1:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                lo = mid + 1
            else:
                hi = mid

        if nums[lo] != target:
            ans[1] = (lo - 1)
        elif nums[hi] != target:
            ans[1] = (hi - 1)
        else:
            ans[1] = (hi)

        return ans

sol = Solution()
print(sol.searchRange([1],1))



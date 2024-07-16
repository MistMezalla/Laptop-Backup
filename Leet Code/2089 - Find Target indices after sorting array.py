class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        left,right = 0,len(nums) - 1

        def low_bound(val,lo,hi):
            while hi - lo > 1:
                mid = (hi+lo)//2

                if nums[mid] == target:
                    hi = mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            else:
                return -1

        def upper_bound(val, lo, hi):
            while hi - lo > 1:
                mid = (hi + lo) // 2

                if nums[mid] == target:
                    lo = mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if nums[hi] == target:
                return hi
            if nums[lo] == target:
                return lo
            else:
                return -1

        left = low_bound(target,0,len(nums)-1)
        left = left if left > -1 else 0
        right = upper_bound(target,0,len(nums)-1)

        return [i for i in range(left,right+1)]

sol = Solution()
print(sol.targetIndices([1,2,5,2,3],4))


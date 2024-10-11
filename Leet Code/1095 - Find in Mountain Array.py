# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lo,hi = 0,mountain_arr.length() - 1

        ind_mountain_arr = None

        while hi - lo > 0:
            mid = (hi + lo)//2

            if mountain_arr.get(mid) <= mountain_arr.get(mid+1):
                lo = mid + 1

            else:
                hi = mid

        ind_mountain_arr = lo

        lo,hi = 0,ind_mountain_arr

        while hi - lo > 0:
            mid = (hi + lo)//2

            if mountain_arr.get(mid) < target:
                lo = mid + 1
            else:
                hi = mid

        if mountain_arr.get(lo) == target:
            return lo

        lo,hi = ind_mountain_arr,mountain_arr.length() - 1
        while hi - lo > 0:
            mid = (hi + lo)//2

            if mountain_arr.get(mid) > target:
                lo = mid + 1
            else:
                hi = mid

        if mountain_arr.get(lo) == target:
            return lo
        return -1

sol = Solution()
print(sol.findInMountainArray(3, [1,2,4,5,2,1]))
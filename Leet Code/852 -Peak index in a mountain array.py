class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo,hi = 0,len(arr) - 1

        while hi - lo > 0:
            mid = (hi+lo)//2

            if arr[mid] <= arr[mid+1]:
                lo = mid + 1
            else:
                hi = mid

        return lo

sol = Solution()
print(sol.peakIndexInMountainArray([10,20,30,98,100,99,98,50]))

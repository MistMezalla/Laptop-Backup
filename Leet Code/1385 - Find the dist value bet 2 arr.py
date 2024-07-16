class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()

        def isValid(num):
            lo, hi = 0, len(arr2) - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if abs(num - arr2[mid]) <= d:
                    return False
                if arr2[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return True

        res_cnt = 0
        for num in arr1:
            if isValid(num):
                res_cnt += 1

        return res_cnt

sol = Solution()
print(sol.findTheDistanceValue(arr1=[-3, 10, 2, 8, 0, 10], arr2=[-9, -1, -4, -9, -8], d=9))

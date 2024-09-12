class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        LIS, res = [], []

        def bisect_right(val):
            lo = 0
            hi = len(LIS)

            while lo < hi:
                mid = (hi + lo) // 2

                if LIS[mid] <= val:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        for obs in obstacles:
            ind = bisect_right(obs)

            if ind == len(LIS):
                LIS.append(obs)
            else:
                LIS[ind] = obs
            res.append(ind + 1)

        return res

sol = Solution()
print(sol.longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))
print(sol.longestObstacleCourseAtEachPosition([2,2,1]))
print(sol.longestObstacleCourseAtEachPosition([1]))


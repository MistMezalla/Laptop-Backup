from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        new_interval = [(interval,ind) for ind,interval in enumerate(intervals)]

        new_interval.sort(key = lambda x: x[0][0])
        st_pts = [elem[0][0] for elem in new_interval]

        res = [-1] * len(intervals)
        for elem in new_interval:
            ind = bisect_left(st_pts,elem[0][1])
            if ind < len(intervals):
                res[elem[1]] = (new_interval[ind][1])

        return res

sol = Solution()
print(sol.findRightInterval(intervals = [[3,4],[2,3],[1,2]]))
print(sol.findRightInterval(intervals = [[1,4],[2,3],[3,4]]))
print(sol.findRightInterval([[2,8],[1,4],[6,7]]))


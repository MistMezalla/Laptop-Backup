class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            last_pt = res[-1]
            if intervals[i][0] <= last_pt[1]:
                last_pt[1] = max(intervals[i][1],last_pt[1])
            else:
                res.append(intervals[i])

        return res

sol = Solution()
print(sol.merge([[1,3]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[5,6]]))

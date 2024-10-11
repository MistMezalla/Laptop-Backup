class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        cover = []
        i = 0

        while i < len(intervals):
            st,end = intervals[i]

            while i < len(intervals)-1 and intervals[i+1][0] == st:
                i+=1
                end = intervals[i][1]

            while i < len(intervals) and intervals[i][1] <= end:
                i+=1

            cover.append((st,end))

        return len(cover)

sol = Solution()
print(sol.removeCoveredIntervals([[0,10],[5,12]]))
print(sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(sol.removeCoveredIntervals([[1,2],[1,4],[3,4]]))

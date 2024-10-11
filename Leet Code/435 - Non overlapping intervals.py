class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        cnt = 0
        end_time = float('-inf')

        for interval in intervals:
            if interval[0] >= end_time:
                cnt += 1
                end_time = interval[1]

        return len(intervals) - cnt

sol = Solution()
print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))

class Solution():
    def isContained(self,intervals: list[(int,int)]) -> bool:
        if not intervals:
            return False

        intervals.sort(key = lambda x: x[0])
        max_end_pt = intervals[0][1]


        for i in range(1,len(intervals)):
            if intervals[i][1] <= max_end_pt:
                return True

            max_end_pt = intervals[i][1]

        return False

sol = Solution()
print(sol.isContained([(1,5),(7,12),(2,10),(4,15)]))


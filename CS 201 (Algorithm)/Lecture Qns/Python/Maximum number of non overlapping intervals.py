class Solution():
    def max_non_overlapping(self,intervals):
        intervals.sort(key = lambda x: x[1])

        #res = [intervals[0]]

        # j = 1
        # for i in range(1,len(intervals)):
        #     while j < len(intervals) and intervals[j][0] <= res[-1][1]:
        #         j+=1
        #     if i == j:
        #         res.append(intervals[i])

        res = []
        end_time = float('-inf')

        for interval in intervals:
            if interval[0] > end_time:
                res.append(interval)
                end_time = interval[1]

        return res

sol = Solution()
print(sol.max_non_overlapping([(6,13),(5,8),(9,12),(2,10),(14,20)]))




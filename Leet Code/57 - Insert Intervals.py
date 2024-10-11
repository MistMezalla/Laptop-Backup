class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
            i+=1
        ans.append(newInterval)

        while i<len(intervals):
            ans.append(intervals[i])
            i+=1

        return ans


sol = Solution()
print(sol.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(sol.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(sol.insert([[1,2],[3,4],[8,10]],[5,7]))
print(sol.insert([],[3,4]))



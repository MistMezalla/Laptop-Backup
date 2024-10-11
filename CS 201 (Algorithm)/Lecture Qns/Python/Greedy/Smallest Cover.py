'''
-> Wrong logic plz refer to 1288_alt sol which handles all the test cases.
'''
class Solution:
    def smallest_cover(self, intervals):
        intervals.sort(key=lambda x: x[0])
        cover = []
        i = 0
        n = len(intervals)

        while i < n:
            start, end = intervals[i]
            while i < n and intervals[i][1] <= end:
                i += 1
            cover.append((start, end))

        return cover

intervals = [(1, 3), (2, 5), (4, 6), (7, 8), (6, 9)]
sol = Solution()
print(sol.smallest_cover(intervals))

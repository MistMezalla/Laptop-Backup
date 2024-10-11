class Solution:
    def min_intervals(self, points):
        points.sort()
        intervals = 0
        i = 0
        n = len(points)

        while i < n:
            intervals += 1
            cover_end = points[i] + 1
            while i < n and points[i] <= cover_end:
                i += 1

        return intervals


points = [0.5, 1.2, 2.9, 2.3, 3.7, 5.6]
sol = Solution()
print(sol.min_intervals(points))

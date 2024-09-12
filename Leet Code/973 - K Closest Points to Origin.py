class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key = lambda x: (x[0]**2 + x[1]**2)**0.5)
        return [points[i] for i in range(k)]

sol = Solution()
print(sol.kClosest( points = [[1,3],[-2,2]], k = 1))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
print(sol.kClosest(points = [[5,7]],k = 1))

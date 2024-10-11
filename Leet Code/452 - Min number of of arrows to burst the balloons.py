class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[1])
        pts = []

        for interval in points:
            if len(pts) == 0:
                pts.append(interval[1])
                continue

            if pts[-1] >= interval[0]:
               continue

            else:
                pts.append(interval[1])

        return len(pts)

sol = Solution()
print(sol.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))




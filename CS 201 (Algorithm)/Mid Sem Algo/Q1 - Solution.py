class My_Solution:
    def min_pts(self,points,intervals):
        intervals.sort(key = lambda x: x[1])

        pts = []
        visited = [-1] * (points[-1] - points[0] + 1)

        for pt in points:
            visited[pt - points[0]] = 0

        for interval in intervals:
            i = interval[1] - points[0]
            if len(pts) == 0:
                while i>=0:
                    if visited[i] == 0:
                        pts.append(i+points[0])
                        break
                    elif visited[i] == 1:
                        break
                    i-=1
                continue

            if pts[-1] >= interval[0]:
                continue

            else:
                while i >= 0:
                    if visited[i] == 0:
                        pts.append(i+points[0])
                        break
                    elif visited[i] == 1:
                        break
                    i-=1

        return pts

sol = My_Solution()
print(sol.min_pts([1, 3, 4, 6, 7],[[1,5],[2,5],[3,6]]))
print(sol.min_pts([1,2,3,4,5,6,7,8,9,10],[[1,2],[4,5],[7,8]]))
print(sol.min_pts([1,2,3,4,5,6],[[1,6],[2,5],[3,4]]))
print(sol.min_pts([1, 2,3,4,5,6,7,8],[[1,3],[4,6],[2,5],[6,8]]))
print(sol.min_pts([1,2,3,4,5,6,7],[[1,4],[2,6],[4,5],[5,7]]))


class Solution_alt:
    def min_pts(self, points, intervals):
        intervals.sort(key=lambda x: x[1])  # Sort intervals by end time
        pts = []
        last_point = float('-inf')

        for interval in intervals:
            if last_point < interval[0]:  # If last point can't cover the interval
                last_point = interval[1]  # Use the end of the current interval
                pts.append(last_point)

        return pts

sol = Solution_alt()
print(sol.min_pts([1, 3, 4, 6, 7], [[1, 5], [2, 5], [3, 6]]))
print(sol.min_pts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [[1, 2], [4, 5], [7, 8]]))
print(sol.min_pts([1, 2, 3, 4, 5, 6], [[1, 6], [2, 5], [3, 4]]))
print(sol.min_pts([1, 2, 3, 4, 5, 6, 7, 8], [[1, 3], [4, 6], [2, 5], [6, 8]]))
print(sol.min_pts([1, 2, 3, 4, 5, 6, 7], [[1, 4], [2, 6], [4, 5], [5, 7]]))


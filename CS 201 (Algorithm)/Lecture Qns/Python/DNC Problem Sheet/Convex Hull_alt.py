class Solution:
    def convex_hull(self, points):
        # Sort points by x-coordinate (and by y-coordinate in case of a tie)
        points = sorted(points)
        return self.hull(points)

    def hull(self, points):
        if len(points) <= 3:
            return self.brute_force_hull(points)

        mid = len(points) // 2
        left_hull = self.hull(points[:mid])
        right_hull = self.hull(points[mid:])

        return self.merge_hulls(left_hull, right_hull)

    def brute_force_hull(self, points):
        # Return the sorted points; they form the hull in case of <= 3 points
        if len(points) < 3:
            return points
        return self.merge_hulls(self.brute_force_hull(points[:len(points)//2]),
                                self.brute_force_hull(points[len(points)//2:]))

    def merge_hulls(self, left_hull, right_hull):
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Find the lower tangent
        i = 0
        j = 0
        while True:
            moved = False
            while cross(right_hull[j], left_hull[i], left_hull[(i + 1) % len(left_hull)]) < 0:
                i = (i + 1) % len(left_hull)
                moved = True
            while cross(left_hull[i], right_hull[j], right_hull[(j - 1) % len(right_hull)]) > 0:
                j = (j - 1) % len(right_hull)
                moved = True
            if not moved:
                break
        lower_tangent = (i, j)

        # Find the upper tangent
        i = len(left_hull) - 1
        j = len(right_hull) - 1
        while True:
            moved = False
            while cross(left_hull[i], right_hull[j], right_hull[(j + 1) % len(right_hull)]) < 0:
                j = (j + 1) % len(right_hull)
                moved = True
            while cross(right_hull[j], left_hull[i], left_hull[(i - 1) % len(left_hull)]) > 0:
                i = (i - 1) % len(left_hull)
                moved = True
            if not moved:
                break
        upper_tangent = (i, j)

        # Combine the hulls along the tangents
        result = []
        i = upper_tangent[0]
        while True:
            result.append(left_hull[i])
            if i == lower_tangent[0]:
                break
            i = (i + 1) % len(left_hull)

        i = lower_tangent[1]
        while True:
            result.append(right_hull[i])
            if i == upper_tangent[1]:
                break
            i = (i + 1) % len(right_hull)

        return result

# Example usage:
sol = Solution()
points1 = [(0, 0), (1, 1), (2, 2), (1, 0), (2, 0), (3, 1), (0, 3)]
print(sol.convex_hull(points1))  # Should output the convex hull points

points2 = [(2, -5), (11, -1), (1, 0), (12, 8), (4, 7), (8, 1), (10, -4), (15, 3),(5,2)]
print(sol.convex_hull(points2))
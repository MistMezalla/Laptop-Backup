# Assuming all points are distinct
class Solution():
    def convex_hull(self,points):
        points.sort()
        return self.hull(points)

    def hull(self,points):
        if len(points) <= 3:
            return self.brute_force(points)

        mid = len(points)//2

        left_half = points[:mid]
        right_half = points[mid:]

        left_hull = self.hull(left_half)
        right_hull = self.hull(right_half)

        return self.merge_hulls(left_hull,right_hull)

    def brute_force(self,points):
        points.sort()
        return points

    def merge_hulls(self, left_hull, right_hull):
        # Finding U.T.
        i = left_hull.index(max(left_hull,key = lambda x: x[0]))
        j = right_hull.index(min(right_hull,key = lambda x: x[0]))
        mid_x = (left_hull[i][0] + right_hull[j][0]) / 2

        while True:
            right_part = self.y_intercept(left_hull[i], right_hull[(j + 1) % len(right_hull)], mid_x)
            curr = self.y_intercept(left_hull[i], right_hull[j], mid_x)
            left_part = self.y_intercept(left_hull[(i - 1) % len(left_hull)], right_hull[j], mid_x)

            if curr is not None:
                if right_part is not None and right_part > curr:
                    j = (j + 1) % len(right_hull)
                elif left_part is not None and left_part > curr:
                    i = (i - 1) % len(left_hull)
                else:
                    break
            else:
                if right_part >= left_part:
                    j = (j + 1) % len(right_hull)
                else:
                    i = (i - 1) % len(left_hull)


        upper_tangent = (i, j)

        # Finding L.T.
        i = left_hull.index(max(left_hull, key=lambda x: x[0]))
        j = right_hull.index(min(right_hull, key=lambda x: x[0]))
        mid_x = (left_hull[i][0] + right_hull[j][0]) / 2

        while True:
            right_part = self.y_intercept(left_hull[i], right_hull[(j - 1) % len(right_hull)], mid_x) #0
            curr = self.y_intercept(left_hull[i], right_hull[j], mid_x) #none
            left_part = self.y_intercept(left_hull[(i + 1) % len(left_hull)], right_hull[j], mid_x) #2
            if curr is not None:
                if right_part is not None and right_part < curr:
                    j = (j - 1) % len(right_hull)
                elif left_part is not None and left_part < curr:
                    i = (i + 1) % len(left_hull)
                else:
                    break
            else:
                if right_part <= left_part:
                    j = (j - 1) % len(right_hull)
                else:
                    i = (i + 1) % len(left_hull)


        lower_tangent = (i, j)

        merged_hull = []
        i = upper_tangent[1]
        while True:
            merged_hull.append(right_hull[i])
            if i == lower_tangent[1]:
                #merged_hull.append(left_hull[lower_tangent[0]])
                break
            i = (i + 1) % len(right_hull)

        i = lower_tangent[0]
        while True:
            merged_hull.append(left_hull[i])
            if i == upper_tangent[0]:
                break
            i = (i + 1) % len(left_hull)

        return merged_hull

    def y_intercept(self, p1, p2, mid_x):
        if p2[0] == p1[0]:
            return None

        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

        return p1[1] + slope * (mid_x - p1[0])
    
    # def merge_hulls(self, left_hull, right_hull):
    #     # Finding U.T.
    #     i = len(left_hull) - 1
    #     j = 0
    #     mid_x = (left_hull[i][0] + right_hull[j][0]) / 2
    #
    #     while True:
    #         yi1 = self.y_intercept(left_hull[i], right_hull[(j + 1) % len(right_hull)], mid_x)
    #         yi2 = self.y_intercept(left_hull[i], right_hull[j], mid_x)
    #
    #         if yi1 > yi2 or (yi1 == yi2 and right_hull[(j + 1) % len(right_hull)][1] > right_hull[j][1]):
    #             j = (j + 1) % len(right_hull)
    #         else:
    #             yi1 = self.y_intercept(left_hull[(i - 1) % len(left_hull)], right_hull[j], mid_x)
    #             if yi1 > yi2 or (yi1 == yi2 and left_hull[(i - 1) % len(left_hull)][1] > left_hull[i][1]):
    #                 i = (i - 1) % len(left_hull)
    #             else:
    #                 break
    #
    #     upper_tangent = (i, j)
    #
    #     # Finding L.T.
    #     i = 0
    #     j = len(right_hull) - 1
    #     mid_x = (left_hull[i][0] + right_hull[j][0]) / 2
    #
    #     while True:
    #         yi1 = self.y_intercept(left_hull[i], right_hull[(j - 1) % len(right_hull)], mid_x)
    #         yi2 = self.y_intercept(left_hull[i], right_hull[j], mid_x)
    #
    #         if yi1 < yi2 or (yi1 == yi2 and right_hull[(j - 1) % len(right_hull)][1] < right_hull[j][1]):
    #             j = (j - 1) % len(right_hull)
    #         else:
    #             yi1 = self.y_intercept(left_hull[(i + 1) % len(left_hull)], right_hull[j], mid_x)
    #             if yi1 < yi2 or (yi1 == yi2 and left_hull[(i + 1) % len(left_hull)][1] < left_hull[i][1]):
    #                 i = (i + 1) % len(left_hull)
    #             else:
    #                 break
    #
    #     lower_tangent = (i, j)
    #
    #     merged_hull = []
    #     i = upper_tangent[1]
    #     while True:
    #         merged_hull.append(right_hull[i])
    #         if i == lower_tangent[1]:
    #             merged_hull.append(left_hull[lower_tangent[0]])
    #             break
    #         i = (i + 1) % len(right_hull)
    #
    #     i = lower_tangent[0]
    #     while True:
    #         merged_hull.append(left_hull[i])
    #         if i == upper_tangent[0]:
    #             break
    #         i = (i + 1) % len(left_hull)
    #
    #     return merged_hull
    #
    # def y_intercept(self, p1, p2, mid_x):
    #     if p2[0] == p1[0]:
    #         # Vertical line case, return the y-value of the point with x = mid_x
    #         if mid_x == p1[0]:
    #             return p1[1]
    #         return float('inf')  # Represents that no valid intercept can be calculated here
    #     else:
    #         slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    #         return p1[1] + slope * (mid_x - p1[0])


sol = Solution()
points1 = [(0, 0), (1, 1), (2, 2), (1, 0), (2, 0), (3, 1), (0, 3)]
print(sol.convex_hull(points1))

points2 = [(2, -5), (11, -1), (1, 0), (12, 8), (4, 7), (8, 1), (10, -4), (15, 3),(5,2)]
print(sol.convex_hull(points2))
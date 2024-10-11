'''
-> In this example finding max slopes cross slope 2 calculations is good pt to learn but is redundant wrt this
problem's req.
'''
class Solution():
    def max_slope(self,points):
        if len(points) < 2:
            return float('-inf')

        points.sort()

        mid = len(points) // 2
        left_half = points[:mid]
        right_half = points[mid:]

        max_slope_left = self.max_slope(left_half)
        max_slope_right = self.max_slope(right_half)

        min_y_left = min(left_half, key=lambda p: p[1])
        # max_y_left = max(left_half, key=lambda p: p[1])
        # min_y_right = min(right_half, key=lambda p: p[1])
        max_y_right = max(right_half, key=lambda p: p[1])

        cross_slope_1 = float('-inf')
        if max_y_right[0] != min_y_left[0]:
            cross_slope_1 = (max_y_right[1] - min_y_left[1]) / (max_y_right[0] - min_y_left[0])

        # cross_slope_2 = float('-inf')
        # if min_y_right[0] != max_y_left[0]:
        #     cross_slope_2 = (min_y_right[1] - max_y_left[1]) / (min_y_right[0] - max_y_left[0])

        return max(max_slope_left, max_slope_right, cross_slope_1)#, cross_slope_2)


sol = Solution()
P = [(1, 3), (2, 8), (3, 4), (4, 10), (2,7), (1,12), (5,6)]
print("Maximum slope:", sol.max_slope(P))


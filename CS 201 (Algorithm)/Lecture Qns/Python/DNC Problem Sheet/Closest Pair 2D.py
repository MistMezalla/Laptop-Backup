class Solution():
    def closest_pair(self,points):
        points_x = sorted(points,key = lambda x: x[0])
        points_y = sorted(points,key = lambda x: x[1])
        return self.min_dist(points_x, points_y)

    def min_dist(self,points_x,points_y):
        n = len(points_x)
        if n <= 3:
            return self.brute_force_dist(points_x)

        mid = n//2
        mid_pt = points_x[mid]

        left_x = points_x[:mid]
        right_x = points_x[mid:]

        left_y = []
        right_y = []

        for pt in points_y:
            if pt[0] <= mid_pt[0]:
                left_y.append(pt)
            else:
                right_y.append(pt)

        left_min_dist = self.min_dist(left_x,left_y)
        right_min_dist = self.min_dist(right_x,right_y)

        dist_min = min(left_min_dist,right_min_dist)

        strip_pts = [pt for pt in points_x if abs(pt[0] - mid_pt[0]) < dist_min]

        strip_min_dist = float('inf')
        for i in range(len(strip_pts)):
            for j in range(i+1,min(i+7,len(strip_pts))):
                if strip_pts[j][1] - strip_pts[i][1] >= dist_min:
                    continue
                strip_min_dist = min(strip_min_dist,self.euclidean_dist(strip_pts[i],strip_pts[j]))


        return min(strip_min_dist,dist_min)

        # How to convert to 7 box search in linear time?
    def brute_force_dist(self,points):
        dist_min = float('inf')

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist_min = min(dist_min,self.euclidean_dist(points[i],points[j]))

        return dist_min

    def euclidean_dist(self,p1,p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


sol = Solution()
points1 = [(2, -5), (11, -1), (1, 0), (12, 8), (4, 7), (8, 1), (10, -4), (5, 2), (15, 3)]
print(sol.closest_pair(points1))
points2 = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
print(sol.closest_pair(points2))
points3 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3)]
print(sol.closest_pair(points3))
points4 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
print(sol.closest_pair(points4))
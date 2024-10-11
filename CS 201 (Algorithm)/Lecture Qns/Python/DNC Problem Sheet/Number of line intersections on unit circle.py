class Solution1(): # O(nlog^2n)
    def merge_count_split_inv(self,arr):
        # This function performs the merge step and counts the inversions
        if len(arr) < 2:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = self.merge_count_split_inv(arr[:mid])
        right, inv_right = self.merge_count_split_inv(arr[mid:])

        merged, split_inv = self.merge_and_count(left, right)

        total_inversions = inv_left + inv_right + split_inv
        return merged, total_inversions


    def merge_and_count(self,left, right):
        # Merging two sorted arrays and counting the number of split inversions
        result = []
        i = j = 0
        inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                # Every time an element from right is added before left, it is an inversion
                inversions += len(left) - i

        result.extend(left[i:])
        result.extend(right[j:])

        return result, inversions


    def count_intersections(self,p_points, q_points):
        # Step 1: Sort the points on the circle by their polar angle (angles in radians)
        n = len(p_points)

        # Sort p_points based on their angle
        p_sorted = sorted(range(n), key=lambda i: p_points[i])

        # Map the sorted p_points to their corresponding q_points
        q_mapped = [q_points[i] for i in p_sorted]

        # Step 2: Count the number of inversions in the q_mapped array
        _, num_intersections = self.merge_count_split_inv(q_mapped)

        return num_intersections


    # Example usage
import math
sol1 = Solution1()
# Sample points on the unit circle, represented by angles (in radians)
# These points represent the positions of p_points and q_points on the unit circle.
p_points = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
q_points = [math.pi, 3 * math.pi / 4, math.pi / 2, math.pi / 4, 0]

# Counting the number of intersecting line segments
num_intersections = sol1.count_intersections(p_points, q_points)
print("Number of intersecting line segments:", num_intersections)

from sortedcontainers import SortedList
class Solution2:#O(nlogn)
    def count_inversions_bst(self,arr):
        # Use a balanced BST (SortedList) to count inversions in O(n log n)
        sorted_list = SortedList()
        inversions = 0
        for value in arr:
            # Count how many elements in sorted_list are greater than the current value
            inversions += len(sorted_list) - sorted_list.bisect_right(value)
            # Add the current value to the sorted_list
            sorted_list.add(value)
        return inversions

    def count_intersections_optimized(self,p_points, q_points):
        n = len(p_points)

        # Step 1: Sort p_points by their angles
        p_sorted = sorted(range(n), key=lambda i: p_points[i])

        # Step 2: Map q_points to their corresponding sorted p_points
        q_mapped = [q_points[i] for i in p_sorted]

        # Step 3: Count inversions using BST (this gives the number of intersections)
        num_intersections = self.count_inversions_bst(q_mapped)

        return num_intersections

sol2 = Solution2()
# Sample points on the unit circle, represented by angles (in radians)
p_points = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
q_points = [math.pi, 3 * math.pi / 4, math.pi / 2, math.pi / 4, 0]

# Counting the number of intersecting line segments
num_intersections = sol2.count_intersections_optimized(p_points, q_points)
print("Number of intersecting line segments:", num_intersections)


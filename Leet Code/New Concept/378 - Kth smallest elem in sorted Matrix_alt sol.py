'''
-> My sol:- (Correct)
    -> T(n) = O(log(max_val - min_val) * nlogn)

-> Below sol:-
    -> My sol failed to harness upon the fact that 'both rows and cols' are simultaneously sorted in non - decreasing
    order.
    -> This sol makes use of this fact and improves on the search time of elem_less function to (m+n); where m and n
    are dimensions of the matrix
'''
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while hi - lo > 0:
            mid = (hi + lo)//2

            if self.elem_less(matrix,mid) < k:
                lo = mid+1
            else:
                hi = mid

        return lo

    def elem_less(self,matrix,val):
        cnt = 0
        col = len(matrix) - 1

        for row in range(len(matrix)):
            while col >= 0 and matrix[row][col] > val:
                col -= 1
            cnt += col + 1

        return cnt

sol = Solution()
print(sol.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(sol.kthSmallest([[-5]], k = 1))
print(sol.kthSmallest([[1,4,8,10],[2,5,9,12],[7,7,9,12],[8,8,10,13]],9))

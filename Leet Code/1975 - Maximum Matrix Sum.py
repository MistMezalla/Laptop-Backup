class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        neg = []
        max_neg = -(10**5+10)
        sum_max = 0
        is_zero = False
        abs_min = 10**5+10

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                num = matrix[i][j]

                if abs(num) <= abs_min:
                    abs_min = abs(num)

                if num == 0:
                    is_zero = True

                if num < 0:
                    neg.append(num)
                    if num >= max_neg:
                        max_neg = num

                sum_max += abs(num)

        if is_zero or len(neg) % 2==0:
            max_neg = 0
        else:
            max_neg = -abs_min

        print(abs_min)

        return sum_max + 2*max_neg

sol = Solution()
print(sol.maxMatrixSum([[1,-1],[-1,1]]))
print(sol.maxMatrixSum([[1,2,3],[1,2,3],[1,2,3]]))
print(sol.maxMatrixSum([[-1,2,3],[1,2,3],[1,-2,3]]))
print(sol.maxMatrixSum([[1,-2,3],[-1,2,3],[1,2,-3]]))
print(sol.maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]]))



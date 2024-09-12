class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        col = len(matrix[0]) - 1
        for row in range(len(matrix)):
            while col >= 0 and matrix[row][col] > target:
                col -= 1
            if matrix[row][col] == target:
                return True

        return False

sol = Solution()
print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))
print(sol.searchMatrix(matrix = [[1,4,6,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 3))

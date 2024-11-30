'''
-> Well I mistook the def of val that cell represents
    -> For clarity pl read supplementary material
'''

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        dp = [[0]*(len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j]) + 1
                    res += dp[i+1][j+1]

        return res

sol = Solution()
print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(sol.countSquares([[1,1,1,1],[1,0,1,1],[0,1,1,1]]))
print(sol.countSquares([[1,1,1,1],[1,1,1,1],[0,1,1,1]]))
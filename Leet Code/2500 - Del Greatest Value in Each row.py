class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for i in range(0, len(grid)):
            grid[i].sort()
        n = len(grid[0])
        res = 0
        for j in range(0, n):
            max_elem = float('-inf')
            for i in range(0, len(grid)):
                max_elem = max(max_elem, grid[i].pop())
            res += max_elem

        return res

sol = Solution()
print(sol.deleteGreatestValue([[1,2,4],[3,3,1]]))
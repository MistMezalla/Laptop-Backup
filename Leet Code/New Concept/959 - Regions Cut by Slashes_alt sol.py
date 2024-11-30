class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        exp_grid = [[0]*3*n for _ in range(3*n)]

        for i in range(n):
            for j in range(n):
                r = i *3
                c = j * 3

                if grid[i][j] == "\\":
                    exp_grid[r][c] = 1
                    exp_grid[r+1][c+1] = 1
                    exp_grid[r+2][c+2] = 1

                elif grid[i][j] == "/":
                    exp_grid[r][c+2] = 1
                    exp_grid[r+1][c+1] = 1
                    exp_grid[r+2][c] = 1

        cnt = 0

        visited = [[0]*3*n for _ in range(3*n)]

        def isValid(r,c):
            return 0 <= r < 3*n and 0 <= c < 3 * n

        def dfs(r,c):
            visited[r][c] = 1

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx, c+dy

                if isValid(new_r,new_c) and exp_grid[new_r][new_c] == 0 and not visited[new_r][new_c]:
                    dfs(new_r,new_c)

        for r in range(3*n):
            for c in range(3*n):
                if not visited[r][c] and exp_grid[r][c] == 0:
                    dfs(r, c)
                    cnt += 1

        return cnt

sol = Solution()
print(sol.regionsBySlashes(grid = [" /","/ "]))
print(sol.regionsBySlashes([" /","\\/"]))
print(sol.regionsBySlashes([" \\","\\/"]))
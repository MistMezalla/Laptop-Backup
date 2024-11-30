class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(r,c):
            visited[r][c] = 1

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx,c + dy

                if isValid(new_r,new_c) and grid[new_r][new_c] == "1" and not visited[new_r][new_c]:
                    dfs(new_r,new_c)

        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    cnt += 1

        return cnt

sol = Solution()
print(sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["0","0","1","1","1"]
]))

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        perimeter = 0

        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            visited[r][c] = 1
            nonlocal perimeter

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_r,new_c = r+dx,c+dy

                if not isValid(new_r,new_c):
                    perimeter += 1

                elif grid[new_r][new_c] == 0:
                    perimeter += 1

                elif not visited[new_r][new_c]:
                    dfs(new_r,new_c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and not visited[r][c]:
                    dfs(r,c)

        return perimeter

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

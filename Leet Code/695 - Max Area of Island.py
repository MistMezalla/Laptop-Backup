class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            nonlocal curr_area
            visited[r][c] = 1
            curr_area += 1

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx, c + dy

                if isValid(new_r,new_c) and grid[new_r][new_c] and not visited[new_r][new_c]:
                    dfs(new_r,new_c)

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                curr_area = 0
                if grid[r][c] and not visited[r][c]:
                    dfs(r,c)
                    max_area = max(max_area,curr_area)

        return max_area

sol = Solution()
print(sol.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
                                  [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                                  [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))



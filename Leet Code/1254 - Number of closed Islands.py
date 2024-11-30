class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            visited[r][c] = 1

            is_closed = True
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx, c + dy

                if not isValid(new_r,new_c):
                    is_closed = False

                elif grid[new_r][new_c] == 0 and not visited[new_r][new_c]:
                    is_closed &= dfs(new_r,new_c)
                # if isValid(new_r,new_c) and
                #     dfs(new_r,new_c)

            return is_closed

        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and not visited[r][c]:
                    if dfs(r,c):
                        cnt += 1

        return cnt

sol = Solution()
print(sol.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))

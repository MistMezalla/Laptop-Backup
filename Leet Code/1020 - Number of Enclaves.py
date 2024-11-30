class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        visited = [[0]* len(grid[0]) for _ in range(len(grid))]

        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            visited[r][c] = 1

            nonlocal curr_enclaves
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx,c+dy

                if not isValid(new_r,new_c):
                    curr_enclaves += 5000
                elif not visited[new_r][new_c] and grid[new_r][new_c]:
                    curr_enclaves += 1
                    dfs(new_r,new_c)
                # if isValid(new_r,new_c) and not visited[new_r][new_c] and grid[new_r][new_c]:
                #     dfs(new_r,new_c)



        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] and not visited[r][c]:
                    curr_enclaves = 1
                    dfs(r,c)
                    cnt += curr_enclaves if curr_enclaves < 5000 else 0

        return cnt

sol = Solution()
print(sol.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

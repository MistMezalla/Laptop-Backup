class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        visited = [[0]*len(grid1[0]) for _ in range(len(grid1))]

        def isValid(r,c):
            return 0 <= r < len(grid1) and 0 <= c < len(grid1[0])

        def dfs1(r,c,col):
            visited[r][c] = 1
            grid1[r][c] = col

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx, c + dy

                if isValid(new_r,new_c) and grid1[new_r][new_c] and not visited[new_r][new_c]:
                    dfs1(new_r,new_c,col)

        def dfs2(r,c,col):
            visited[r][c] = 1
            is_sub_island = 1
            if col != grid1[r][c]:
                is_sub_island = 0

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
                new_r, new_c = r + dx, c + dy

                if isValid(new_r, new_c) and grid2[new_r][new_c] and not visited[new_r][new_c]:
                    is_sub_island &= dfs2(new_r, new_c, col)

            return is_sub_island

        col = 1
        for r in range(len(grid1)):
            for c in range(len(grid1[r])):
                if grid1[r][c] and not visited[r][c]:
                    dfs1(r,c,col)
                    col += 1

        visited = [[0]*len(grid2[0]) for _ in range(len(grid2))]

        cnt = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[r])):
                if grid2[r][c] and not visited[r][c] and grid1[r][c]:
                    if (dfs2(r,c,grid1[r][c])):
                        cnt += 1

        return cnt

sol = Solution()
print(sol.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
                          grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))

print(sol.countSubIslands( grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
                           grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))

print(sol.countSubIslands([[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],
                           [0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]],
                          [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],
                           [1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]))



        
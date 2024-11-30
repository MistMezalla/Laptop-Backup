class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = [[0]*len(image[0]) for _ in range(len(image))]

        def isValid(r,c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])

        def dfs(r,c,val,col):
            visited[r][c] = 1
            image[r][c] = col

            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c = r + dx, c + dy

                if isValid(new_r,new_c) and image[new_r][new_c] == val and not visited[new_r][new_c]:
                    dfs(new_r,new_c,val,col)

        dfs(sr,sc,image[sr][sc],color)

        return image

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,4))
print(sol.floodFill([[0,0,0],[0,0,0]],0,0,0))
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,3))
print(sol.floodFill([[1,1,0,0],[1,0,0,1],[0,1,0,1],[0,1,1,1]],1,1,4))
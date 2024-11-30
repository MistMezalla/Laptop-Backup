class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        visited = [[False] * len(land[0]) for _ in range(len(land))]
        res = []

        def isValid(r, c):
            return 0 <= r < len(land) and 0 <= c < len(land[0])

        def dfs(r1, c1, r2, c2):
            visited[r1][c1] = True
            r2, c2 = max(r2, r1), max(c2, c1)

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r, c = r1 + dx, c1 + dy
                if isValid(r, c) and not visited[r][c] and land[r][c]:
                    r2, c2 = dfs(r, c, r2, c2)
            return r2, c2

        for r1 in range(len(land)):
            for c1 in range(len(land[r1])):
                if land[r1][c1] and not visited[r1][c1]:
                    r2, c2 = dfs(r1, c1, r1, c1)
                    res.append([r1, c1, r2, c2])

        return res

sol = Solution()
print(sol.findFarmland([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(sol.findFarmland([[1,1,0,0],[0,0,1,1],[0,0,1,1]]))
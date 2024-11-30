#using bottom up dp
class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        max_moves = 0
        for j in range(1,n):
            for i in range(m):
                if i > 0 and grid[i][j] > grid[i-1][j-1] and dp[i-1][j-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)

                if grid[i][j] > grid[i][j-1] and dp[i][j-1]:
                    dp[i][j] = max(dp[i][j],dp[i][j-1] + 1)

                if i < m-1 and grid[i][j] > grid[i+1][j-1] and dp[i+1][j-1]:
                    dp[i][j] = max(dp[i][j],dp[i+1][j-1] + 1)

                max_moves = max(max_moves,dp[i][j] - 1)

        return max_moves

from collections import deque
# using bfs
class Solution_alt:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        moves = [-1,0,1]

        def isValid(i,j,val):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] > val:
                    return True
            return False

        max_moves = 0
        for k in range(n):
            queue = deque()
            start = grid[k][0]
            queue.append((start,k,0))
            adj_list = {start: []}
            visited = {start: True}
            level = {start: 0}

            while queue:
                node,i,j = queue.popleft()

                for move in moves:
                    i += move
                    j += 1

                    if isValid(i,j,node):
                        adj_list[node].append(grid[i][j])
                        visited[grid[i][j]] = False
                        level[grid[i][j]] = -1

                    i -= move
                    j-= 1

                for neighbour in adj_list[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        level[neighbour] = level[node] + 1
                        queue.append((neighbour,i,j))


            max_moves = max(max_moves,max(list(level.keys())))

        return max_moves

sol = Solution()
print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
print(sol.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))


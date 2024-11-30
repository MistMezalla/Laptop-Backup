'''
-> This is an alt sol for my failed attempt of writing bfs based sol
'''
from collections import deque
class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        moves = [-1,0,1]

        visited = [[0]*n for _ in range(m)]

        queue = deque()
        max_moves = 0
        for i in range(m):
            visited[i][0] = 1
            queue.append((i,0,0))  #row,col,cnt

        while queue:
            for i in range(len(queue)):
                r,c,cnt = queue.popleft()

                max_moves = max(max_moves,cnt)
                for move in moves:
                    new_r,new_c = r+move,c+1

                    if 0<= new_r < m and 0 <= new_c < n and grid[new_r][new_c] > grid[r][c]:
                        if not visited[new_r][new_c]:
                            visited[new_r][new_c] = 1
                            queue.append((new_r,new_c,cnt+1))

        return max_moves


sol = Solution()
print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
print(sol.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))


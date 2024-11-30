from collections import deque
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        cost = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(0, 0, 0)])  # cost, r, c
        cost[0][0] = 0

        def isValid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        while queue:
            curr_cost, r, c = queue.popleft()

            for ind, (dr, dc) in enumerate(dir):
                new_r, new_c = r + dr, c + dc

                if isValid(new_r, new_c):
                    new_cost = curr_cost if grid[r][c] == ind + 1 else curr_cost + 1

                    if new_cost < cost[new_r][new_c]:
                        cost[new_r][new_c] = new_cost

                        if grid[r][c] == ind + 1:
                            queue.appendleft((new_cost, new_r, new_c))
                        else:
                            queue.append((new_cost, new_r, new_c))

        return cost[len(grid) - 1][len(grid[0]) - 1]

# Test
sol = Solution()
print(sol.minCost(grid=[[1, 1, 3], [4, 3, 2]]))  # Output: 1

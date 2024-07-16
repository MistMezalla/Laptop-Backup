class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        st = len(grid[0]) - 1

        lvl = 0
        cnt = 0
        end = st
        st -= 1
        while lvl < len(grid):
            for _ in range(st,-1,-1):
                if grid[lvl][st] >= 0:
                    break
                st -= 1
            cnt += end - st if grid[lvl][end] < 0 else 0
            lvl += 1

        return cnt

sol = Solution()
print(sol.countNegatives(grid = [[3,-1,-3,-3,-3],[2,-2,-3,-3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]]))

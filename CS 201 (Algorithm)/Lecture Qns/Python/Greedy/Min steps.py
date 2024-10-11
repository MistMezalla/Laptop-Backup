from collections import deque

class Solution:
    def min_steps(self, n):
        queue = deque([(1,0)]) # num,step req to reach num
        visited = set()

        while queue:
            num,steps = queue.popleft()

            next_num1 = num+1
            if next_num1 == n:
                return steps + 1
            elif next_num1 not in visited:
                visited.add(next_num1)
                queue.append((next_num1,steps+1))

            next_num2 = num * 2
            if next_num2 == n:
                return steps + 1
            elif next_num2 not in visited:
                visited.add(next_num2)
                queue.append((next_num2,steps + 1))

sol = Solution()
print(sol.min_steps(10))
print(sol.min_steps(12))
print(sol.min_steps(7))
print(sol.min_steps(18))

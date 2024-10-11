from collections import deque
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()

        for ch in s:
            if stack and ch == "]" and  stack[-1] == "[":
                stack.pop()
                continue

            stack.append(ch)

        return (len(stack)//2 + 1 )//2
sol = Solution()
print(sol.minSwaps("[]"))
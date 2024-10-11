from collections import deque
class Solution:
    def minLength(self, s: str) -> int:
        stack = deque()

        for ch in s:
            if stack and ((ch == "B" and stack[-1] == "A") or (ch=="D" and stack[-1] == "C")):
                stack.pop()

            else:
                stack.append(ch)

        return len(stack)

sol = Solution()
print(sol.minLength("ABFCACDB"))
print(sol.minLength("AAACCCDDDBBBB"))
print(sol.minLength("D"))



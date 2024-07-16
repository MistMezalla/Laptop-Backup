from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        map = dict(zip(("(",")","{","}","[","]"),(3,-3,2,-2,1,-1)))
        print(map)
        stack = deque()

        for char in s:
            if map[char]>0:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if map[stack[-1]] + map[char] != 0:
                    return False
                stack.pop()

        if len(stack):
            return False
        return True

sol = Solution()
print(sol.isValid("{([)}"))






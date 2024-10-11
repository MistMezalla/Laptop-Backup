from collections import deque
class Solution:
    #using stack
    # def minAddToMakeValid(self, s: str) -> int:
    #     stack = deque()
    #
    #     for ch in s:
    #         if stack and ch == ")" and stack[-1] == "(":
    #             stack.pop()
    #             continue
    #         stack.append(ch)
    #
    #     return len(stack)

    # using const space
    def minAddToMakeValid(self, s: str) -> int:
        cnt_op = 0
        cnt_cl = 0

        for ch in s:
            if ch == "(":
                cnt_op += 1
            else:
                if cnt_op > 0:
                    cnt_op -= 1
                else:
                    cnt_cl += 1

        return cnt_op + cnt_cl



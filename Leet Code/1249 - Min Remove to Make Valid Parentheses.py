from collections import deque
class Solution:
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     # Deque Based
    #     Deque = deque()
    #
    #     for i in range(len(s)):
    #         if Deque and s[i] == ")" and s[Deque[-1]] == "(":
    #             Deque.pop()
    #             continue
    #
    #         if s[i] in "()":
    #             Deque.append(i)
    #
    #     res = ""
    #     for i in range(len(s)):
    #         if Deque and i == Deque[0]:
    #             Deque.popleft()
    #             continue
    #         res += s[i]
    #
    #     return res
    #
    # Const Space
    def minRemoveToMakeValid(self, s: str) -> str:
        op_cnt = 0
        op = 0
        cl = 0

        for ch in s:
            if ch == "(":
                op += 1
                op_cnt += 1
            elif ch == ")":
                if op > 0:
                    op-=1
                else:
                    cl += 1

        op = op_cnt - op

        res = ""
        for ch in s:
            if cl > 0 and ch == ")":
                cl -= 1
            elif op > 0 and ch == "(":
                op -= 1
                res += ch
            elif op == 0 and ch == "(":
                continue
            else:
                res+=ch

        return res
sol = Solution()
print(sol.minRemoveToMakeValid(s = "lee(t(c)o)de)"))


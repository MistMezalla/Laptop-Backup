class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        s = []

        def generate(s, open: int, close: int):
            if open == 0 and close == 0:
                return res.append("".join(s))

            if open > 0:
                s.append("(")
                generate(s,open-1,close)
                s.pop()

            if close > 0:
                if open < close:
                    s.append(")")
                    generate(s,open,close-1)
                    s.pop()

        generate(s,n,n)

        return res


sol = Solution()
print(sol.generateParenthesis(2))


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                continue
            else:
                if not found:
                    found = True
                else:
                    return False

        return True

sol = Solution()
print(sol.checkOnesSegment("101101"))
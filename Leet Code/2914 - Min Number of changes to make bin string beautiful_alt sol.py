'''
-> Check 1st my code and then editorial to understand the optimised code below
'''
class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i+1] for i in range(0,len(s),2))

sol = Solution()
print(sol.minChanges("110001100111"))
print(sol.minChanges("1100011110011000110001110000"))
print(sol.minChanges("1001"))
print(sol.minChanges("10"))
print(sol.minChanges("0000"))
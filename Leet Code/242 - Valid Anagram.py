class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s=list(s)
        t=list(t)

        t.sort()
        s.sort()

        s = "".join(s)
        t = "".join(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True


my_sol = Solution()
print(my_sol.isAnagram("rat","car"))
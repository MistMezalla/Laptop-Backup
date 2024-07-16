'''
Used Hashing :  identical literal from 't' count was subtracted(instead of adding) from hash map of s.
'''
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] -= 1
            else:
                return False

        l = list(d.values())

        for i in range(len(l)):
            if (l[i]):
                return False

        return True


my_sol = Solution()
print(my_sol.isAnagram("aa","bb"))
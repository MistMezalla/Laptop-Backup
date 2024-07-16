class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d_f = {}
        d_r = {}
        l = s.split()

        if len(l) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d_f:
                if d_f[pattern[i]] != l[i]:
                    return False
            else:
                d_f[pattern[i]] = l[i]

        for j in range(len(pattern)):
            if l[j] in d_r:
                if d_r[l[j]] != pattern[j]:
                    return False
            else:
                d_r[l[j]] = pattern[j]

        return True


my_sol = Solution()
print(my_sol.wordPattern("abba","dog dog dog dog"))


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lps = [0] * len(s)

        len_longest_prefix = 0
        i = 1
        while i < len(s):
            if s[i] == s[len_longest_prefix]:
                len_longest_prefix += 1
                lps[i] = len_longest_prefix
                i+=1

            else:
                if len_longest_prefix != 0:
                    len_longest_prefix = lps[len_longest_prefix-1]
                else:
                    lps[i] = 0
                    i+=1

        m = 0
        for i,val in enumerate(lps):
            if val * 2 - 1 == i:
                m = val

        if m == 0:
            return False

        substr = s[:m]

        i = 0
        j = 0
        n = len(s)

        res = []
        while i < n:
            if s[i] == substr[j]:
                i+=1
                j+=1

            if j == m:
                res.append(i-j)
                j = lps[j-1]

            elif i < n and substr[j] != s[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1

        expected_res = [i for i in range(len(s)) if i % m == 0]
        if res == expected_res:
            return True
        return False

sol = Solution()
print(sol.repeatedSubstringPattern("ababab"))
print(sol.repeatedSubstringPattern("abaababaab"))
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        lps = self.build_lps(needle)

        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1

            if j == m:
                return i - j

            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1

        return -1
    def build_lps(self,pattern):
        lps = [0] * len(pattern)

        len_longest_prefix = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[len_longest_prefix]:
                len_longest_prefix += 1
                lps[i] = len_longest_prefix
                i+=1

            else:
                if len_longest_prefix != 0:
                    len_longest_prefix = lps[len_longest_prefix-1]
                else:
                    lps[i] = 0
                    i+=1

        return lps

sol = Solution()
print(sol.strStr( haystack = "sadbutsad", needle = "sad"))



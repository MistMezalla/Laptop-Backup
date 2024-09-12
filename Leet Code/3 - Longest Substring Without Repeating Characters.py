class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()

        st = 0
        max_len = 0
        for end in range(len(s)):
            if s[end] not in str_set:
                str_set.add(s[end])

            else:
                while st<len(s) and s[end] in str_set:
                    str_set.remove(s[st])
                    st += 1
                str_set.add(s[end])

            max_len = max(max_len,end - st + 1)

        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abcdefghijal"))


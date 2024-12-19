class Solution:
    def maximumLength(self, s: str) -> int:
        seen_map = {s[0] : 1}

        temp_substr = s[0]
        for i in range(1,len(s)):
            if s[i] == temp_substr[-1]:
                seen_map[temp_substr] += 1
                temp_substr += s[i]

            else:
                temp_substr = s[i]

            if temp_substr not in seen_map:
                seen_map[temp_substr] = 1
            else:
                seen_map[temp_substr] += 1

        max_len = -1
        for substr,freq in seen_map.items():
            if freq >= 3:
                max_len = max(max_len,len(substr))

        return max_len

sol = Solution()
print(sol.maximumLength("abcbbaabbccaaaa"))
print(sol.maximumLength("aaa"))
print(sol.maximumLength("aaaa"))








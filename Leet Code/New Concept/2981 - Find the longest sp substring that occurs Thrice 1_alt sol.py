'''
-> below code is improvement over my logic which fails for some test cases provided in my code.
'''

class Solution:
    def maximumLength(self, s: str) -> int:
        freq = [[0]*(len(s) + 1) for _ in range(26)]

        prev_chr = s[0]
        sub_len = 1
        freq[ord(prev_chr) - ord("a")][sub_len] = 1

        res = -1
        for i in range(1,len(s)):
            curr_chr = s[i]

            if prev_chr == curr_chr:
                sub_len += 1
                freq[ord(curr_chr) - ord("a")][sub_len] += 1

            else:
                prev_chr = curr_chr
                sub_len = 1
                freq[ord(curr_chr) - ord("a")][sub_len] += 1

        for i in range(26):
            for length in range(len(s)-1,0,-1):
                freq[i][length] += freq[i][length + 1]
                
                if freq[i][length] >= 3:
                    res = max(res,length)
                    break

        return res

sol = Solution()
print(sol.maximumLength("abcbbaabbccaaaa"))
print(sol.maximumLength("aaaa"))
print(sol.maximumLength("aaaaaa"))
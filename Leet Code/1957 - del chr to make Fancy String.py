class Solution:
    def makeFancyString(self, s: str) -> str:
        sim_chr_cnt = [1]*len(s)

        res = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                sim_chr_cnt[i] += sim_chr_cnt[i-1]

            if sim_chr_cnt[i] < 3:
                res += s[i]

        return res

sol = Solution()
print(sol.makeFancyString("leeettaaabaaaate"))
print(sol.makeFancyString("aaaabaa"))
print(sol.makeFancyString("aabatteece"))

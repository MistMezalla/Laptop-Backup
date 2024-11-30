class Solution:
    def compressedString(self, word: str) -> str:
        res = ""

        cnt = 1
        ch = word[0]
        for i in range(1,len(word)):
            if word[i] == ch:
                cnt += 1

                if cnt > 9:
                    res += str(cnt - 1) + ch
                    cnt = 1
            else:
                res += str(cnt) + ch
                cnt = 1
                ch = word[i]

        res += str(cnt) + ch

        return res

sol = Solution()
print(sol.compressedString("abcde"))
print(sol.compressedString("aaaaaaaaaaaaaabb"))
print(sol.compressedString("aaaaaaaabbcccccaaaaaaaaaaaafaeee"))
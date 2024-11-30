class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        ch = chars[0]
        cnt = 1
        for i in range(1,len(chars)):
            if chars[i] == ch:
                cnt += 1

            else:
                if cnt > 1:
                    s += ch + str(cnt)
                else:
                    s += ch
                cnt = 1
                ch = chars[i]

        if cnt > 1:
            s += ch + str(cnt)
        else:
            s += ch

        n = len(s)
        for i in range(n):
            chars[i] = s[i]

        for _ in range(len(chars) - n):
            chars.pop()

        return n

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
print(sol.compress(["a"]))
print(sol.compress(["a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))


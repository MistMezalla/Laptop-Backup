class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        l = []
        for i in range(ord(s[0]),ord(s[3])+1):
            for j in range(int(s[1]),int(s[4])+1):
                st = chr(i)
                l.append(st+str(j))

        return l


sol = Solution()
print(sol.cellsInRange("K1:L2"))
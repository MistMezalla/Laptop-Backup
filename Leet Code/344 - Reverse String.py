class Solution:
    def reverseString(self, s: list[str]) -> None:
        if (len(s)%2 == 1):
            for i in range(len(s)//2 + 1):
                s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
        else:
            for i in range(len(s)//2):
                s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]


sol = Solution()
s=["H"," ","a","n"," ","n","a"," "," ","h"]
print(s)
sol.reverseString(s)
print(s)

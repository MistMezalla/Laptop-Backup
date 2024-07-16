class Solution1:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

class Solution2:
    def checkOnesSegment(self, s: str) -> bool:
        s=s.strip("0")
        print(s)
        return "0" not in s

sol2 = Solution2()
print(sol2.checkOnesSegment("110"))
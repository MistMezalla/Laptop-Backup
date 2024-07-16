class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0])-ord('a'))%2 == (ord(coordinates[1])-ord('0'))%2:
            return True
        else:
            return False


sol = Solution()
print(sol.squareIsWhite("h3"))
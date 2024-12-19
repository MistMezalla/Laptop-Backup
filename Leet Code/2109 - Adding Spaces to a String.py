class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = ""

        i = 0
        for ind,ch in enumerate(s):
            if i < len(spaces) and ind == spaces[i]:
                res += " " + ch
                i += 1

            else:
                res += ch

        return res

sol = Solution()
print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))

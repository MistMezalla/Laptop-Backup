class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ch_s= ""
        ch_g=""
        diff = False
        swap =  False
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i] != goal[i]:
                if swap:
                    return False
                if not (ch_s or ch_g):
                    ch_s = goal[i]
                    ch_g = s[i]
                    diff = True
                elif s[i] == ch_s and goal[i] == ch_g:
                    diff = False
                    swap = True
                else:
                    return False


        if len(set(s)) != len(s):
            if diff:
                return False
            else:
                return True
        else:
            if swap:
                return True
            else:
                return False


sol = Solution()
print(sol.buddyStrings("ab","ab"))
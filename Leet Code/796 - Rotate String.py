class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        new_s = s + s[:len(s)-1]

        n = len(new_s)
        m = len(goal)


        lps = self.lps_arr(goal)
        i=0
        j=0

        while i < n:
            if new_s[i] == goal[j]:
                i+=1
                j+=1

            if j == m:
                return True

            elif i < n and goal[j] != new_s[i]:
                if j != 0:
                    j = lps[j-1]

                else:
                    i+=1

        return False


    def lps_arr(self,pattern):
        lps = [0]*len(pattern)

        len_longest_prefix = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[len_longest_prefix]:
                len_longest_prefix += 1
                lps[i] = len_longest_prefix
                i += 1

            else:
                if len_longest_prefix != 0:
                    len_longest_prefix = lps[len_longest_prefix-1]

                else:
                    lps[i] = 0
                    i += 1

        return lps

sol = Solution()
print(sol.rotateString("abcde","cdeab"))

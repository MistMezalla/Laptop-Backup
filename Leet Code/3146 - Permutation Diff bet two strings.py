class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d_s = {}

        for i in range(len(s)):
            d_s[s[i]] = i

        sum = 0
        for i in range(len(t)):
            sum += abs(i - d_s[t[i]])

        return sum

    
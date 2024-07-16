class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = len(word1)
        R = len(word2)

        res = ''
        i = j = k = 0
        while i<L and j<R:
            if k%2 == 0:
                res+=word1[i]
                i+=1
            else:
                res+=word2[j]
                j+=1
            k+=1

        while i<L:
            res += word1[i]
            i += 1

        while j<R:
            res += word2[j]
            j += 1

        return res




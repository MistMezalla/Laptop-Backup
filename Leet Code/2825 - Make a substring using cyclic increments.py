class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        i = 0
        j = 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i+=1
                j+=1
            elif (ord(str2[j]) - ord(str1[i])) == 1:
                i += 1
                j += 1
            elif str2[j] == "a" and str1[i] == "z":
                i+=1
                j+=1
            else:
                i+=1

        return j == len(str2)

sol =  Solution()
print(sol.canMakeSubsequence("zc","ad"))

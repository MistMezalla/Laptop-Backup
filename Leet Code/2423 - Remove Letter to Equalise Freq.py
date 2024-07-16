class Solution:
    def equalFrequency(self, word: str) -> bool:
        hash = [0]*26

        for char in word:
            hash[ord(char) - ord("a")]+=1

        hash = [elem for elem in hash if elem != 0]

        if hash.count(max(hash)) == 1 or hash.count(min(hash)) == 1:
            if len(set(hash)) > 2:
                return False
            elif len(set(hash)) == 2:
                if min(hash) == max(hash) - 1:
                    return True
                elif min(hash) == 1 and hash.count(min(hash)) < 2:
                    return True
                else:
                    return False


            else:
                return True
        else:
            if max(hash) == 1:
                return True
            return False

sol = Solution()

print(sol.equalFrequency("aaccdde")) #T
print(sol.equalFrequency("aaccdd")) #F
print(sol.equalFrequency("acd")) #T Wrong
print(sol.equalFrequency("aacd")) #T
print(sol.equalFrequency("aac")) #T
print(sol.equalFrequency("aaaccdde")) #F
print(sol.equalFrequency("aaccddef")) #F

print(sol.equalFrequency("ceeeec"))


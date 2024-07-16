'''
-> No diff approach than mine.
-> analyse the test cases properly
-> coding will take hardly 10 mins
-> don't give more than "45 min"
-> resolve the tricky ones within the time limit and that to try to solve with 100% accuracy.
'''

class Solution:
    def equalFrequency(self, word: str) -> bool:
        hash = [0]*26

        for char in word:
            hash[ord(char) - ord("a")]+=1

        hash = [elem for elem in hash if elem!=0]

        if len(set(hash)) > 2:
            return False
        elif len(set(hash)) == 1:
            if max(hash)==1:
                return True
            elif len(hash) == 1:
                return True
            else:
                return False
        else:
            ind = hash.index(min(hash))
            hash[ind]-=1

            rem = False
            if 0 in hash:
                hash.remove(0)
                rem = True

            if len(set(hash))==1:
                return True

            if rem:
                hash.append(1)
            else:
                hash[ind]+=1
            hash[hash.index(max(hash))]-=1

            if len(set(hash))==1:
                return True
            else:
                return False


sol = Solution()
print(sol.equalFrequency("aaccdde")) #T
print(sol.equalFrequency("aaccdd")) #F
print(sol.equalFrequency("acd")) #T Wrong
print(sol.equalFrequency("aacd")) #T
print(sol.equalFrequency("aac")) #T
print(sol.equalFrequency("aaaccdde")) #F
print(sol.equalFrequency("aaccddef")) #F
print(sol.equalFrequency("ceeeec")) #F
print(sol.equalFrequency("zz")) #
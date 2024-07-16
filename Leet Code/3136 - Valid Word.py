class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False

        vow="aeiouAEIOU"

        if not word.isalnum():
            return False

        v=c=0
        for char in word:
            if char in vow:
                v+=1
            elif char.isalpha() and char not in vow:
                c+=1

        if v*c:
            return True
        return False

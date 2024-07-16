class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        hash = [0]*26

        for i in range(len(words)):
            for char in words[i]:
                hash[ord(char)-ord('a')]+=1


        for i in range(26):
            if hash[i]%len(words) != 0:
                return False

        return True

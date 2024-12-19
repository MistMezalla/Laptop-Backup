class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for ind,word in enumerate(sentence):
            ans = self.KMP_string_matching(word,searchWord)

            if ans:
                return ind + 1

        return -1

    def KMP_string_matching(self, text: str, pattern: str) -> list[int]:
        n = len(text)
        m = len(pattern)

        lps = self.lps_array_construction(pattern)
        res = []

        i = 0
        j = 0
        while i < n:
            if text[i] == pattern[j]:
                i+=1
                j+=1

            if j == m:
                res.append(i-j)
                j = lps[j-1]  #Shifted by j - (length of longest proper prefix of the pattern at index j)

            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]  #Shifted by j - (length of longest proper prefix of the pattern at index j)
                else:
                    i+=1

        return res

    def lps_array_construction(self,pattern: str):
        lps = [0] * len(pattern)

        len_longest_prefix = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[len_longest_prefix]:
                len_longest_prefix+=1
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
print(sol.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
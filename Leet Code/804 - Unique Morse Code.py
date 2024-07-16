class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for i in range(len(words)):
            st = ''
            for char in words[i]:
                ind = ord(char) - ord('a')
                st += morse_code[ind]
            words[i] = st

        return len(set(words))

sol = Solution()
print(sol.uniqueMorseRepresentations(["gin","zen","gig","msg"]))

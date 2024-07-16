class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()

        for i in range(len(sentence)):
            if sentence[i][0] not in "aeiouAEIOU":
                sentence[i] = sentence[i][1:] + sentence[i][0]

            sentence[i]+="ma"
            sentence[i]+=(i+1)*"a"

        return " ".join(sentence)
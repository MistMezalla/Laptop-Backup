class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()

        for i in range(len(sentence)):
            if sentence[i%len(sentence)][-1] != sentence[(i+1)%len(sentence)][0]:
                return False

        return True



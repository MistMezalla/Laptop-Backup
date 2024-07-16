class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        num = 0
        for elem in patterns:
            if elem in word:
                num += 1

        return num
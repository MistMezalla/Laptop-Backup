'''
Made use of concept of generators in this code.
'''


class Solution:
    def firstPalindrome(self, a: list[str]) -> str:
        return next((w for w in a if w==w[::-1]),'')
'''
The definition of "subsequence" is sneaky in this problem. Apparently, a subsequence doesn't have to be continuous
in the original string.

"A string is a subsequence of a given string, if it is generated by deleting some characters of a given string
without changing its order."

Algorithm:
Given two alphabet a and b. At most two operations are required, one to delete all a and another to delete all b.
But if the input string is already empty, no operation is necessary; if the input string is palindrome, 1 operation
is enough.
'''

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        elif s == s[::-1]:
            return 1
        return 2

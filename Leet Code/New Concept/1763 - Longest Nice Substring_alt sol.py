'''
-> Intuition of this code:-
    -> Hashing via set
        -> For constant time access for case complement search
    -> DnC
'''


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""

        str_set = set(s)

        for i,c in enumerate(s):
            if c.swapcase() not in str_set:
                left_str = self.longestNiceSubstring(s[:i])
                right_str = self.longestNiceSubstring(s[i+1:])
                return max(left_str,right_str,key = len)

        return s

sol = Solution()
print(sol.longestNiceSubstring( s = "YaBaAaybZ"))
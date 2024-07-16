'''
-> If k is odd, it is the same as the symbol at position (k+1)/2 in the previous row, coz it corresponds to the first
child of the parent symbol.
-> If k is even, it is the same as the symbol at position (k)/2 in the previous row, coz it corresponds to the second
child of the parent symbol, which is the inverse of the parent symbol.

-> The 1st symbol in the 1st row is 0.
->So, the 2nd symbol in the 2nd row is derived from the 1st symbol in the 1st row:
->Since 2 is even, it is the inverse of the parent symbol (0).
->Thus, the 2nd symbol in the 2nd row is 1.
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent_index = (k+1)//2

        parent_val = self.kthGrammar(n-1,parent_index)

        if k % 2 == 1:
            return parent_val
        else:
            return 1 - parent_val

sol = Solution()
print(sol.kthGrammar(4,5))
print(sol.kthGrammar(1,1))
print(sol.kthGrammar(2,1))
print(sol.kthGrammar(2,2))

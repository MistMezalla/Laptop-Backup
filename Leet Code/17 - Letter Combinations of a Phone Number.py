'''
-> Below code complexity:-
    -> T(n) = O(n*4**n)
        -> in worst case there can be 4 letters associated to a number of dial
        -> for each combination so generated, O(n) time to generate string out of the list by join method
    -> S(n) = O(n * 4**n)
        -> simply becoz of space req to store the res list.
'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        comb = []
        hash_dig = {'2' : "abc",'3': "def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':'tuv','9':"wxyz"}
        if len(digits) == 0:
            return res

        def gen_comb(comb,st):
            for i in range(len(hash_dig[digits[st]])):
                comb.append(hash_dig[digits[st]][i])
                if len(comb) == len(digits):
                    res.append("".join(comb))

                if st + 1 < len(digits):
                    gen_comb(comb,st+1)
                comb.pop()

        gen_comb(comb,0)
        return res

sol = Solution()
print(sol.letterCombinations("2"))
print(sol.letterCombinations("23"))
print(sol.letterCombinations("234"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("9"))
print(sol.letterCombinations("97"))
'''
-> The extra O(n) associated with join method can be avoided by adding comb(which is str here) on fly with new char
    -> this helps to handle the complexity associated with pop char from str.

-> The term "on fly" => that while giving recursive function call send a new variable of comb + new_letter instead of
updating comb
-> This will reduce the need to pop char from comb(as not updated during rec call) when backtracked
'''
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        if len(digits) == 0:
            return res

        hash_dig = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': 'tuv', '9': "wxyz"}
        def gen_comb(st,comb):
            if st == len(digits):
                res.append(comb)
                return

            for letter in hash_dig[digits[st]]:
                gen_comb(st+1,comb + letter)


        gen_comb(0,"")
        return res

sol = Solution()
print(sol.letterCombinations("2"))
print(sol.letterCombinations("23"))
print(sol.letterCombinations("234"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("9"))
print(sol.letterCombinations("97"))
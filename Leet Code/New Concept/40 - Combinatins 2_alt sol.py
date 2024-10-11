'''
-> Refer My sol to get the understanding
    -> In the commented part I tried to the same logic of the part of sol that inherited from other's sol using
    while loop and increasing i until I skip all these bunch of duplicates
    -> The condition I used is that comb is empty and current elem is eq to prev elem
        -> The abv condition is also eqv to cond i > st(comb empty also sim)

    -> Another blunder is that my while loop logic fails to handle a bunch of duplicates ahead of the deleted ones
        -> See test case 2 of qns description.
'''

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []
        candidates.sort()

        def gen_combination_sum(st):
            if sum(comb) == target:
                res.append(comb[:])
                return

            for i in range(st,len(candidates)):
                if i > st and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                if sum(comb) <= target:
                    gen_combination_sum(i+1)
                else:
                    comb.pop()
                    break
                comb.pop()

        gen_combination_sum(0)
        return res

sol = Solution()
print(sol.combinationSum2([1,1,1,1,1,1,1],9))
print(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5))
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(sol.combinationSum2([1,2,3,4,5,6,7,8,9],45))
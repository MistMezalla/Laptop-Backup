class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []
        candidates.sort()

        def gen_combinations(st):
            if sum(comb) == target and comb not in res:
                res.append(comb[:])
                return

            for i in range(st,len(candidates)):
            # i = st
            # while i < len(candidates):
            #     if not comb and i > 0 and candidates[i-1] == candidates[i]:
            #         while candidates[i] == candidates[i-1]:
            #             i+=1
                if i > st and candidates[i] == candidates[i - 1]: # This part is referred
                    continue
                comb.append(candidates[i])
                if sum(comb) <= target:
                    gen_combinations(i+1)
                else:
                    comb.pop()
                    break
                comb.pop()
                # i+=1

        gen_combinations(0)
        return res

sol = Solution()
print(sol.combinationSum2([1,1,1,1,1,1,1],9))
print(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5))
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))



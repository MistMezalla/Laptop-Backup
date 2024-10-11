class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        comb = []
        candidates.sort()

        def gen_comb_sum(st):
            if sum(comb) == target:
                res.append(comb[:])
                return

            for i in range(st,len(candidates)):
                # if comb and comb[-1] <= candidates[i]:
                #     comb.append(candidates[i])
                # elif not comb:
                #     comb.append(candidates[i])
                # else:
                #     continue
                comb.append(candidates[i])

                if sum(comb) <= target:
                    gen_comb_sum(i)

                else:
                    comb.pop()
                    break
                comb.pop()


        gen_comb_sum(0)
        return res

sol = Solution()
print(sol.combinationSum([2,3,6,7],7))

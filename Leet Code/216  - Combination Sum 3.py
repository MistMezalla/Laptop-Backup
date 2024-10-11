class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        comb = []
        nums = [1,2,3,4,5,6,7,8,9]

        def gen_comb_sum(st):
            if len(comb) == k and sum(comb) == n:
                res.append(comb[:])
                return

            for i in range(st,len(nums)):
                comb.append(nums[i])
                if sum(comb) <= n:
                    gen_comb_sum(i+1)
                else:
                    comb.pop()
                    break
                comb.pop()


        gen_comb_sum(0)
        return res

sol = Solution()
print(sol.combinationSum3(3,7))
print(sol.combinationSum3( k = 3, n = 9))
print(sol.combinationSum3(k = 9, n = 45))

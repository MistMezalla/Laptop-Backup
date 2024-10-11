class Solution:
    # def combine(self, n: int, k: int) -> list[list[int]]:
    #     res = []
    #     visited = [[0] * (n+1) for _ in range(n+1)]
    #
    #     for i in range(1,n+1):
    #         comb = [i]
    #
    #         def gen_combinations(comb):
    #             if len(comb) == k:
    #                 res.append(comb[:])
    #                 return
    #
    #             for j in range(i+1,n+1):
    #                 # if visited[i][j] == 1:
    #                 #     continue
    #
    #                 if j <= comb[-1]:
    #                     continue
    #                 # visited[i][j] = 1
    #                 comb.append(j)
    #                 gen_combinations(comb)
    #                 comb.pop()
    #                 # visited[i][j] = 0
    #
    #         gen_combinations(comb)
    #     return res

        # alt sol: helper outside for loop
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = []

        def gen_combinations(st):
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(st,n+1):
                comb.append(i)
                gen_combinations(i+1)
                comb.pop()

        gen_combinations(1)

        return res

# sol = Solution()
# print(sol.combine(4,2))
# print(sol.combine(4,3))
# print(sol.combine(5,2))
# print(sol.combine(5,3))

# Follow up Qn:-
'''
-> return the combinations of i/p of form [1,1,1,2,2,3,4] where an elem can appear more than once
    -> o/p for the abv i/p = [[1,1],[2,2],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] where k == 2
'''

#from collections import Counter
class Solution_Follow_Up:
    def combine(self,nums: list[int], k: int)-> list[list[int]]:
        nums.sort()
        # cnt_num = Counter(nums)

        res = []
        # for num in cnt_num:
        #     if cnt_num[num] >= k:
        #         res.append([num,num])
        cnt = 1
        i = 0
        n = len(nums) - 1
        while i < n:
            if nums[i] == nums[i+1]:
                cnt+= 1
                if cnt == k+1:
                    nums.pop(i)
                    n-= 1
                    cnt -= 1
                    continue
            if nums[i] != nums[i+1]:
                cnt = 1
            i += 1

        comb = []
        def gen_combinations(st):
            if len(comb) == k and comb not in res:
                res.append(comb[:])
                return

            for i in range(st,len(nums)):
                comb.append(nums[i])
                gen_combinations(i+1)
                comb.pop()

        gen_combinations(0)
        return res

sol = Solution_Follow_Up()
print(sol.combine([1,1,1,1,2,2,3,4],2))


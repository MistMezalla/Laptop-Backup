class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def gen_subsets(st,subset):
            res.append(subset[:])

            for i in range(st,len(nums)):
                subset.append(nums[i])
                gen_subsets(i+1,subset)
                subset.pop()

        gen_subsets(0,[])

        res = [tuple(x) for x in res]
        set_res = set(res)
        res = [list(x) for x in set_res]
        return res

    # def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    #     res = []
    #     nums.sort()
    #     tuple_nums = [(num,i) for i,num in enumerate(nums)]
    #     visited = [0]*len(nums)
    #
    #     def gen_subsets(st,subset):
    #         res.append(subset[:])
    #
    #         for i in range(st,len(nums)):
    #             if i > 0:
    #                 if nums[i-1] != nums[i]:
    #                     subset.append(nums[i])
    #                     visited[i] += 1
    #                 elif visited[i-1] != 0:
    #                     subset.append(nums[i])
    #                     visited[i] += 1
    #             else:
    #                 subset.append(nums[i])
    #                 visited[i] += 1
    #
    #             gen_subsets(i+1,subset)
    #             subset.pop()
    #             visited[i] -= 1
    #
    #     gen_subsets(0,[])
    #     return res


sol = Solution()
print(sol.subsetsWithDup([1,2,2,1]))

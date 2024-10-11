class Solution:
    # def permuteUnique(self, nums: list[int]) -> list[list[int]]:
    #     res = []
    #     nums_tuple = [(num, i) for i, num in enumerate(nums)]
    #
    #     def gen_permutations(permutation, indices):
    #         if len(permutation) == len(nums) and permutation not in res:
    #             res.append(permutation[:])
    #
    #         for i in range(len(nums)):
    #             if nums_tuple[i][1] in indices:
    #                 continue
    #
    #             permutation.append(nums_tuple[i][0])
    #             indices.append(nums_tuple[i][1])
    #             gen_permutations(permutation, indices)
    #             permutation.pop()
    #             indices.pop()
    #
    #     gen_permutations([], [])
    #     return res
    #
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        visited = [0] * len(nums)

        def gen_permutation(permutation):
            if len(permutation) == len(nums) and permutation not in res:
                res.append(permutation[:])

            for i in range(len(nums)):
                if visited[i]:
                    continue

                visited[i] = 1
                permutation.append(nums[i])
                gen_permutation(permutation)
                visited[i] = 0
                permutation.pop()

        gen_permutation([])
        return res


sol = Solution()
print(sol.permuteUnique([1, 1, 2]))


# Note:-
'''
-> Not all O(n**2) sol are deemed to be bad
-> Depending upon the brute force T(n) O(n**2) can be optimal sol.
-> In this qn brute force T(n) = n! = sqrt(2*pi*n)(n/e)**n => expo in nature
-> Hence a O(n**2) sol will be deemed optimal in this case
-> But sol below != O(n**2) but == O(n**2 x n!)
    -> O(n**2) work for checking if st when combined with for loop.
'''


class Solution:
    # def permute(self, nums: list[int]) -> list[list[int]]:
    #     res = []
    #
    #     def gen_permutations(permutation):
    #         if len(permutation) == len(nums):
    #             res.append(permutation[:])
    #             return
    #
    #         for i in range(len(nums)):
    #             if nums[i] in permutation:
    #                 continue
    #
    #             permutation.append(nums[i])
    #             gen_permutations(permutation)
    #             permutation.pop()
    #
    #     gen_permutations([])
    #     return res

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        visited = [0] * len(nums)

        def gen_permutations(permutation):
            if len(permutation) == len(nums):
                res.append(permutation[:])

            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = 1
                permutation.append(nums[i])
                gen_permutations(permutation)
                visited[i] = 0
                permutation.pop()

        gen_permutations([])
        return res



sol = Solution()
print(sol.permute([1,2,3]))

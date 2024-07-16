'''
-> Wrt to my approach the backtracking is accomplished vai the means of "for loop" and not "2 ptrs" as done in case
of "generate parenthesis" qn.
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def generate(st,elem):
            res.append(elem[:])

            for i in range(st,len(nums)):
                elem.append(nums[i])

                generate(i+1,elem)

                elem.pop()

        generate(0,[])

        return res

sol = Solution()
print(sol.subsets([1,2,3]))

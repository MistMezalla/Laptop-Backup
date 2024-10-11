'''
-> Wrt to my approach the backtracking is accomplished vai the means of "for loop" and not "2 ptrs" as done in case
of "generate parenthesis" qn.
'''

# Another imp Note
'''
-> When the subset in the below qn wld hv been str(immutable data type) then any how the subset will be 'passed by
val'. 
-> Hence both methods(for loops) are equally efficient 
    -> Little modification is req in for loop1
        -> for i in range(st, len(nums)):
            subset += str(nums[i])    # Won't actually mutate `subset` in place
            gen_subsets(i + 1, subset)
            subset = subset[:-1]       # Backtracking by slicing off the last character
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def gen_subsets(st,subset):
            res.append(subset[:])

            # for i in range(st,len(nums)):
            #     subset.append(nums[i])
            #     gen_subsets(i+1,subset)
            #     subset.pop()

            for i in range(st,len(nums)):
                gen_subsets(i + 1, subset + [nums[i]])

        gen_subsets(0,[])
        return res

sol = Solution()
print(sol.subsets([1,2,3]))


# nums=[1,2,3]
# nums.extend([4])
# print(nums)

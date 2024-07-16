'''
-> This logic is fine but needs a bit refinement as it is not able to backtrack properly to generate all the
subsets
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        power = []
        nums.sort()
        i = 0
        j = len(nums)-1
        elem = []

        def generate(sub: list,i,j):
            if i < len(nums):
                if (len(sub) != 0 and nums[i] < sub[-1]):
                    return
                sub.append(nums[i])
                power.append(sub[:])
                generate(sub,i+1,j)
                sub.pop()

            if j>-1:
                if j>i:
                    if (len(sub) != 0 and nums[i] < sub[-1]):
                        return
                    sub.append(nums[j])
                    power.append(sub[:])
                    generate(sub, i, j-1)
                    sub.pop()


        generate(elem,i,j)
        power.append([])

        return power

sol = Solution()
print(sol.subsets([1,2,3]))





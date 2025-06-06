'''
-> Dry Run the logic on pen paper to get the intuition behind the sol
-> Though in qns st it is written to ret indices after sorting, but it is not necessary to sort to ret indices
-> This sol kind of(very loosely) makes use logic behind counting sort
'''
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt = less_than = 0
        for num in nums:
            if num == target:
                cnt+=1
            elif num < target:
                less_than+=1

        res=[]

        for i in range(cnt):
            res.append(less_than)
            less_than += 1

        return res

sol = Solution()
print(sol.targetIndices([1,2,3,2,3],3))


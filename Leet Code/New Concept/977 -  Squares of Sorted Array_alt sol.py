class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0 for i in range(len(nums))]
        l,r = 0 , len(nums)-1

        for i in range(len(nums) -1,-1,-1):
            if abs(nums[l])>=abs(nums[r]):
                val = nums[l]
                l+=1
            else:
                val = nums[r]
                r-=1

            res[i]+=val**2

        return res


sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
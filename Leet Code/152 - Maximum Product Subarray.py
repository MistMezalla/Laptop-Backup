class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        return self.max_product(nums,0,len(nums) - 1)

    def max_product(self,nums: list[int],p: int,r: int):
        if p == r:
            return nums[p]

        q = (p+r)//2

        left_max = self.max_product(nums,p,q)
        right_max = self.max_product(nums,q+1,r)

        left_half = [float('-inf'),float('inf')]
        right_half = [float('-inf'),float('inf')]

        curr_product = 1

        for i in range(q,p-1,-1):
            curr_product *= nums[i]

            left_half[0] = max(curr_product,left_half[0])
            left_half[1] = min(curr_product, left_half[1])

        curr_product = 1

        for i in range(q+1,r+1):
            curr_product *= nums[i]

            right_half[0] = max(curr_product, right_half[0])
            right_half[1] = min(curr_product, right_half[1])

        return max(left_max,right_max,left_half[0]*right_half[0],left_half[1]*right_half[1])


sol = Solution()
print(sol.maxProduct([-2,0,-1]))







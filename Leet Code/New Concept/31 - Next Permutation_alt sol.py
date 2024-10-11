class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        k = 0
        rev_pair = False
        for i in range(len(nums)-2,-1,-1):
            k = i
            if nums[k] < nums[k+1]:
                rev_pair = True
                break

        if not rev_pair:
            nums.reverse()
            print(nums)
            return

        l = 0
        for i in range(len(nums) - 1,-1,-1):
            l = i
            if nums[l] > nums[k]:
                break

        nums[l],nums[k] = nums[k],nums[l]

        #nums[k+1:].reverse()
        nums[k+1:] = reversed(nums[k+1:])

        print(nums)


sol = Solution()
sol.nextPermutation([1,4,3,2])



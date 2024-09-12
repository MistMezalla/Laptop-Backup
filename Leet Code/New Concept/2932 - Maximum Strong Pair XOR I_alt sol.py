class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        nums.sort()

        max_Xor = float('-inf')
        st = 0

        for end in range(len(nums)):
            while st <= end and nums[end] - nums[st] > min(nums[end], nums[st]):
                st += 1
            max_Xor = max(max_Xor,nums[end]^nums[st])

        for i in range(st,len(nums)):
            if nums[-1] - nums[i] <= min(nums[-1], nums[i]):
                max_Xor = max(max_Xor, nums[-1] ^ nums[i])

        return max_Xor

sol = Solution()
print(sol.maximumStrongPairXor([2,3,4,5,1]))


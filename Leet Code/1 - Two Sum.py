class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_ind = {}

        # for ind,num in enumerate(nums):
        #     hash_ind[num] = ind

        for ind,num in enumerate(nums):
            num_complement = target - num

            if num_complement in hash_ind:
                return [ind,hash_ind[num_complement]]

            hash_ind[num] = ind

sol = Solution()
print(sol.twoSum(nums = [7,11,15,-2,2], target = 9))


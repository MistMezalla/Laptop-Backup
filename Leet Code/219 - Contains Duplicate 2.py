class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_ind = {}

        for ind,num in enumerate(nums):
            if num not in hash_ind:
                hash_ind[num] = ind

            else:
                if ind - hash_ind[num] <= k:
                    return True
                hash_ind[num] = ind

        return False

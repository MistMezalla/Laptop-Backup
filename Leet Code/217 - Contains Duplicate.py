class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for i in range(len(nums)):
            if d[nums[i]] > 1:
                return True

        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))




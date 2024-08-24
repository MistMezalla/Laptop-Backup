class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = 0
        elem = None
        for num in nums:
            if cnt == 0:
                elem = num
                cnt+=1
            elif num == elem:
                cnt+=1
            else:
                cnt-=1

        return elem

sol = Solution()
print(sol.majorityElement([1]))

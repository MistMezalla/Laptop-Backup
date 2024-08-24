class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        left_score = [0]*(len(nums))
        right_score = [0]*len(nums)

        min_elem = float('inf')
        length = 0
        for num in nums:
            length += 1
            min_elem = min(min_elem,num)

            left_score[length-1] = min_elem * (length)

        min_elem = float('inf')
        for i in range(len(nums)-1,-1,-1):
            min_elem = min(min_elem,nums[i])

            right_score[i] = min_elem * (len(nums) - i)


        





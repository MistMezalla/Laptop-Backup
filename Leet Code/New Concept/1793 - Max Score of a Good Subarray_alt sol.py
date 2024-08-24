'''
-> My Intuition:-
    -> Well to start from index k and increase the window (sliding window)
    -> store the min_elem and max_score for each window
    -> Stuck on the fact that how to grow the window in O(n) time as i had O(n**2) approach

-> This Code Intuition:-
    -> Same as mine except
    -> Sliding Window in O(n)
'''


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        i = j = k
        min_elem = max_score = nums[k]

        while i > 0 or j < len(nums) - 1:
            if i > 0 and j < len(nums) - 1:
                if nums[i - 1] >= nums[j + 1]: # The imp point of this code
                    i-=1
                else:
                    j+=1

            elif i == 0 and j < len(nums) - 1: #The imp point of this code
                j += 1

            elif j == len(nums) - 1 and i > 0: # The imp point of this code
                i -= 1

            min_elem = min(min_elem,nums[i],nums[j])
            max_score = max(max_score,min_elem * (j - i + 1))

        return max_score



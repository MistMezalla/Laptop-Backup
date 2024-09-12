'''
-> My Intuition:-
    -> Rough idea was akin to sol provided below but didn't have a proper method to combine the logic in parts
    altogether.

-> Sol Intuition:-
    -> Made the use of concepts like
        -> Sliding Window
        -> kth smallest elem (logic)
        -> bin search
    -> First found the bounds of the range sum array to be constructed; lb = min(nums) and ub = sum(nums)
    -> Based on the threshold value passed to sliding window part the window shrinks to be in the constraints
    (here threshold val = one of the range sum values)
    -> Now we use kth smallest elem logic (i,e bin search) to count number of subarryas whose sum are <= threshold
    sum to report only those threshold values that fit well within 'left' and 'right' indices of the range sum
    -> Running Sum Logic (Non trivial part)
        -> We update runningSum by adding array[end] * (end - start + 1). This is because for each new element, we're
        adding it to all existing subarrays ending at the previous index, plus creating a new subarray with just this
        element.
    -> Diff bet running sum and total sum:-
        -> running sum is the sum of all sub arrays ending at 'end' index and starting at index belong to [start,end]
        -> total sum is sum of all possible subarrays(via the means of all sliding window taken into considerations)
        so far
'''
class Solution:
    MODULUS = 10**9 + 7
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        res = self.kth_smallest_range_sum(nums,right) - self.kth_smallest_range_sum(nums,left - 1)

        return res % self.MODULUS
    def kth_smallest_range_sum(self,nums,k):
        lo = min(nums)
        hi = sum(nums)

        while hi - lo > 0:
            mid = (hi + lo)//2

            if self.cnt_range_sum(nums,mid)[0] < k:
                lo = mid + 1
            else:
                hi = mid

        cnt,sum_val = self.cnt_range_sum(nums,lo)
        return sum_val - (cnt - k) * lo
    '''
    -> For the first test case when hi = lo = mid = 13:-
        -> cnt returned is 8 and sum_val = 62 (which included an extra subarray [6,7] whose sum == 13)
        -> thus in order to remove such extra sub arrays (as logic of sliding window checks for subarrays whose sum <= 
        threshold(here bound)
        -> Hence we subtract the extra cnt of subarrays that sum up to lo
    '''

    def cnt_range_sum(self,nums,bound):
        cnt, curr_sum, run_sum, tot_sum = 0,0,0,0

        st = 0
        for end,num in enumerate(nums):
            run_sum += num * (end - st + 1)
            curr_sum += num

            while curr_sum > bound:
                run_sum -= curr_sum
                curr_sum -= nums[st]
                st += 1

            cnt += end - st + 1
            tot_sum += run_sum

        return cnt,tot_sum

sol = Solution()
print(sol.rangeSum([4,3,6,7],4,2,7))
print(sol.rangeSum([4,3,1,2],4,2,5))

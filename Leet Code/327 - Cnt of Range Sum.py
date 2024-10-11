'''
-> Too complex: lots of cases to be handled(#numbre of cases for now limited to test cases avl)
'''
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        self.cnt = 0
        self.pf_sum = [0] * (len(nums) + 1)
        for i in range(1,len(nums) + 1):
            self.pf_sum[i] = self.pf_sum[i-1] + nums[i - 1]

        return self.DnC_cnt(nums,0,len(nums)-1,lower,upper)

    def DnC_cnt(self,nums,left,right,lo,hi):
        if left >= right:
            if lo <= nums[left] <= right:
                self.cnt += 1
            
        mid = (left+right)//2

        left_sum_suff = [0] * (mid - left + 1)
        right_sum_pref = [0] * (right - mid + 1)
        curr_sum = 0

        for i in range(mid,left-1,-1):
            curr_sum += nums[i]
            left_sum_suff[i] = curr_sum

        for i in range(mid,right+1):
            curr_sum += nums[i]
            right_sum_pref[i - mid] = curr_sum



